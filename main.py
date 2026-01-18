from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from models import Base, User, Task, Skill, engine
from schemas import UserCreate, User, TaskCreate, TaskUpdate, Task, SkillCreate, SkillUpdate, Skill, Token, ChatRequest
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
import os
import uuid
from agent.todo_agent import run_todo_agent
from ai_chatbot import ai_chatbot

# Create database tables
Base.metadata.create_all(bind=engine)

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Import database session
from models import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Password hashing functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

# User authentication functions
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user

# Initialize FastAPI app
app = FastAPI(
    title="Todo API",
    description="A simple Todo API with authentication",
    version="1.0.0"
)

# Auth endpoints
@app.post("/api/auth/sign-up", response_model=Token)
def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/api/auth/sign-in", response_model=Token)
def sign_in(user: UserCreate, db: Session = Depends(get_db)):
    # Authenticate user
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/api/auth/logout")
def logout():
    # In a real implementation, you might add the token to a blacklist
    return {"message": "Successfully logged out"}

# Task endpoints
@app.get("/api/tasks/", response_model=list[Task])
def list_tasks(
    skip: int = 0, 
    limit: int = 100, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    tasks = db.query(Task).filter(Task.owner_id == current_user.id).offset(skip).limit(limit).all()
    return tasks

@app.post("/api/tasks/", response_model=Task)
def create_task(
    task: TaskCreate, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        owner_id=current_user.id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/api/tasks/{id}", response_model=Task)
def get_task(
    id: int, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == id, Task.owner_id == current_user.id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task

@app.put("/api/tasks/{id}", response_model=Task)
def update_task(
    id: int, 
    task_update: TaskUpdate, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == id, Task.owner_id == current_user.id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Update task fields
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.completed is not None:
        task.completed = task_update.completed
    
    db.commit()
    db.refresh(task)
    return task

@app.delete("/api/tasks/{id}")
def delete_task(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == id, Task.owner_id == current_user.id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

# Skills endpoints
@app.get("/api/skills/", response_model=list[Skill])
def list_skills(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    skills = db.query(Skill).filter(Skill.owner_id == current_user.id).offset(skip).limit(limit).all()
    return skills

@app.post("/api/skills/", response_model=Skill)
def create_skill(
    skill: SkillCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_skill = Skill(
        name=skill.name,
        description=skill.description,
        proficiency_level=skill.proficiency_level,
        owner_id=current_user.id
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

@app.get("/api/skills/{id}", response_model=Skill)
def get_skill(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    skill = db.query(Skill).filter(Skill.id == id, Skill.owner_id == current_user.id).first()
    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )
    return skill

@app.put("/api/skills/{id}", response_model=Skill)
def update_skill(
    id: int,
    skill_update: SkillUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    skill = db.query(Skill).filter(Skill.id == id, Skill.owner_id == current_user.id).first()
    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )

    # Update skill fields
    if skill_update.name is not None:
        skill.name = skill_update.name
    if skill_update.description is not None:
        skill.description = skill_update.description
    if skill_update.proficiency_level is not None:
        skill.proficiency_level = skill_update.proficiency_level

    db.commit()
    db.refresh(skill)
    return skill

@app.delete("/api/skills/{id}")
def delete_skill(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    skill = db.query(Skill).filter(Skill.id == id, Skill.owner_id == current_user.id).first()
    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )

    db.delete(skill)
    db.commit()
    return {"message": "Skill deleted successfully"}

# AI Chatbot endpoint
@app.post("/api/chatbot/chat/")
async def chat_with_bot(
    message: str,
    conversation_id: Optional[str] = None,
    current_user: User = Depends(get_current_user)
):
    """
    Chat with the AI assistant.

    Args:
        message: The user's message to the chatbot
        conversation_id: Optional conversation ID to continue a conversation
        current_user: The authenticated user

    Returns:
        Response from the AI chatbot with any tool calls executed
    """
    if not message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        # Run the AI agent with the authenticated user's ID
        result = await run_todo_agent(
            user_message=message,
            user_id=str(current_user.id),  # Using the authenticated user's ID
            conversation_id=conversation_id
        )

        return {
            "response": result["response"],
            "conversation_id": result["conversation_id"],
            "tool_calls": result["tool_calls"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")


# Demo user chat endpoint
def verify_jwt(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")

    token = authorization.replace("Bearer ", "")

    # Phase-3 demo decode
    if token == "demo-token":
        return "demo-user"

    raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/api/{user_id}/chat")
def chat(
    user_id: str,
    req: ChatRequest,
    token_user: str = Depends(verify_jwt)
):
    if user_id != token_user:
        raise HTTPException(status_code=403, detail="Forbidden")

    # ✅ AI CHATBOT IS ALLOWED HERE
    response = ai_chatbot.process(
        user_id=user_id,
        message=req.message
    )

    return {
        "response": response
    }