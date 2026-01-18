# Todo Application with MCP Integration

This project implements a comprehensive todo application with AI-powered chatbot functionality using Model Context Protocol (MCP) and multiple AI backends.

## Architecture

The application consists of several interconnected components:

### 1. Main API Server (`main.py`)
- FastAPI-based REST API with authentication
- User management (sign-up, sign-in, logout)
- Task management (CRUD operations)
- Skill management (CRUD operations)
- AI chatbot endpoint that integrates with the agent

### 2. MCP Server (`mcp_server.py`)
- Implements Model Context Protocol for standardized AI tool integration
- Provides task management tools (add, list, update, complete, delete)
- Uses the same underlying database as the main application
- Built with FastMCP for easy integration

### 3. AI Agent (`agent/todo_agent.py`)
- Uses Cohere's AI models for natural language processing
- Integrates with MCP tools for task management
- Maintains conversation history
- Handles tool calling and execution

### 4. Database Layer (`models.py`, `mcp_tools/todo_tools.py`)
- Dual database configuration (SQLAlchemy and SQLModel)
- User, Task, and Skill models
- Conversation and Message models for chat history

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install additional requirements for MCP:
```bash
pip install mcp-tools openai cohere sqlmodel
```

3. Set up environment variables:
```bash
export COHERE_API_KEY="your-cohere-api-key"
export OPENAI_API_KEY="your-openai-api-key"  # if using OpenAI
export DATABASE_URL="sqlite:///./todo_app.db"  # or your preferred database
```

4. Initialize the database:
```bash
python init_db.py
```

## Running the Application

### Option 1: Main API Server
```bash
uvicorn main:app --reload --port 8000
```

### Option 2: MCP Server (for AI tool integration)
```bash
python run_mcp_server.py
```

### Option 3: Both together
The main API server includes the MCP functionality mounted at `/mcp`.

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

## Environment Variables

- `COHERE_API_KEY` - Cohere API key for AI agent
- `OPENAI_API_KEY` - OpenAI API key (if using OpenAI instead of Cohere)
- `DATABASE_URL` - Database connection string
- `SECRET_KEY` - Secret key for JWT tokens (default: "your-secret-key-change-in-production")

## Features

- Secure user authentication with JWT tokens
- Full CRUD operations for tasks and skills
- AI-powered chatbot that can manage tasks through natural language
- Standardized tool integration via Model Context Protocol
- Conversation history tracking
- Support for multiple AI backends (currently Cohere, with OpenAI integration available)

## Development

The project uses:
- FastAPI for the web framework
- SQLAlchemy for ORM (main app)
- SQLModel for ORM (MCP tools)
- SQLite as the default database (can be changed)
- Cohere for AI capabilities
- Model Context Protocol for standardized AI tool integration