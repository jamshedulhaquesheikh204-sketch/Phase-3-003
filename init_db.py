"""Database Initialization Script"""

from sqlmodel import SQLModel
from mcp_tools.todo_tools import Task, Conversation, Message
from sqlmodel import create_engine
import os


# Use the same database configuration as in todo_tools
DATABASE_URL = os.getenv("NEON_DB_URL") or os.getenv("DATABASE_URL") or "sqlite:///./todo_app.db"
engine = create_engine(DATABASE_URL)


def create_tables():
    """Create all database tables."""
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables()