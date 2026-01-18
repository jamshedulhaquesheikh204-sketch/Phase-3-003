# Todo Full-Stack Web Application - Phase III

This is a complete full-stack Todo application with a Next.js frontend and FastAPI backend, featuring JWT authentication, Neon PostgreSQL database, and AI-powered chatbot with Model Context Protocol (MCP) integration.

## Architecture Overview

- **Frontend**: Next.js 14 with App Router
- **Backend**: FastAPI with SQLAlchemy ORM
- **Database**: SQLite/Neon PostgreSQL
- **Authentication**: JWT-based with custom implementation
- **AI Integration**: Cohere-powered chatbot with MCP tools

## Features

- Create, read, update, and delete todos
- Toggle completion status
- JWT-based authentication and authorization
- User isolation (users can only access their own todos)
- AI-powered chatbot that can manage tasks through natural language
- Model Context Protocol (MCP) for standardized AI tool integration
- Skill management alongside task management
- Responsive UI

## Tech Stack

### Frontend
- Next.js 14 (App Router)
- React 18
- TypeScript
- Tailwind CSS

### Backend
- Python 3.13+
- FastAPI
- SQLAlchemy (with some SQLModel for MCP tools)
- Pydantic
- JWT for authentication
- Cohere for AI capabilities
- Model Context Protocol (MCP) for standardized tool integration

### Database
- SQLite (default) or Neon PostgreSQL
- SQLAlchemy ORM

## Environment Variables

Create a `.env.local` file in the root directory with the following variables:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
BETTER_AUTH_URL=http://localhost:3000
```

For the backend, create a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///./todo_app.db  # or postgresql://username:password@host:port/dbname
NEON_DB_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
SECRET_KEY=your-secret-key-change-in-production
COHERE_API_KEY=your-cohere-api-key
OPENAI_API_KEY=your-openai-api-key  # if using OpenAI
```

## Setup Instructions

### Backend Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
pip install mcp-tools openai cohere sqlmodel
```

2. Set up environment variables in `.env` file

3. Initialize the database:
```bash
python init_db.py
```

4. Start the backend server:
```bash
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`

### Running the MCP Server Separately (Optional)

If you want to run the MCP server separately:
```bash
python run_mcp_server.py
```

## API Endpoints

### Authentication
- `POST /api/auth/sign-up` - Create new user
- `POST /api/auth/sign-in` - Login
- `POST /api/auth/logout` - Logout

### Tasks
- `GET /api/tasks/` - List tasks
- `POST /api/tasks/` - Create task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

### Skills
- `GET /api/skills/` - List skills
- `POST /api/skills/` - Create skill
- `GET /api/skills/{id}` - Get specific skill
- `PUT /api/skills/{id}` - Update skill
- `DELETE /api/skills/{id}` - Delete skill

### AI Chatbot
- `POST /api/chatbot/chat/` - Chat with AI assistant

### MCP Endpoint
- `/mcp` - Model Context Protocol endpoint for AI tools

## Authentication

The application uses JWT tokens with a custom implementation. The backend verifies these tokens using the shared secret.

## Database Schema

### User Table
- `id`: Integer (Primary Key)
- `email`: String (Unique, Indexed)
- `hashed_password`: String
- `created_at`: DateTime

### Task Table
- `id`: Integer (Primary Key)
- `title`: String (Indexed)
- `description`: String (Nullable)
- `completed`: Boolean (Default: false)
- `owner_id`: Integer (Indexed, Foreign-key-like behavior)
- `created_at`: DateTime
- `updated_at`: DateTime

### Skill Table
- `id`: Integer (Primary Key)
- `name`: String (Indexed)
- `description`: String (Nullable)
- `proficiency_level`: Integer (Default: 1)
- `owner_id`: Integer (Indexed, Foreign-key-like behavior)
- `created_at`: DateTime
- `updated_at`: DateTime

## AI Integration

The application includes an AI chatbot powered by Cohere that can:
- Add tasks using natural language
- List tasks
- Update tasks
- Complete tasks
- Delete tasks

The AI integration uses Model Context Protocol (MCP) for standardized tool calling, allowing the AI to interact with the application's functionality in a structured way.

## Development

### Running Tests

Various test files are available:
```bash
python test_chatbot.py
python test_api.py
python comprehensive_test.py
```

### Project Structure

```
.
├── agent/                  # AI agent implementation
│   └── todo_agent.py       # Cohere-powered todo agent
├── mcp_tools/             # MCP tools implementation
│   ├── todo_tools.py      # SQLModel-based tools
│   └── chat_models.py     # Chat model definitions
├── main.py                # Main FastAPI application
├── mcp_server.py          # MCP server implementation
├── run_mcp_server.py      # MCP server runner
├── models.py              # SQLAlchemy models
├── database.py            # Database configuration
├── init_db.py             # Database initialization
├── test_*.py              # Various test files
└── requirements.txt       # Dependencies
```

## Deployment

### Backend Deployment
- Deploy to a cloud platform that supports Python (Heroku, Railway, etc.)
- Ensure environment variables are set in deployment environment
- Run database migrations on deploy

### Frontend Deployment
- Deploy to Vercel, Netlify, or similar platform
- Set environment variables in deployment environment

## Security Considerations

- JWT tokens are validated using a shared secret
- Users can only access their own tasks and skills
- Input validation is performed at the service layer
- SQL injection is prevented by using SQLAlchemy ORM
- API keys are stored in environment variables

## Troubleshooting

1. **Backend won't start**: Ensure all environment variables are set correctly
2. **Database connection fails**: Verify DATABASE_URL is correct
3. **Authentication fails**: Check that SECRET_KEY is set correctly
4. **AI features not working**: Verify COHERE_API_KEY is set correctly
5. **MCP tools not working**: Check that the MCP server is running and accessible

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request