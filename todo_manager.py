from typing import List, Dict, Optional
from datetime import datetime
import re

class TodoItem:
    def __init__(self, id: int, title: str, completed: bool = False, due_date: Optional[str] = None):
        self.id = id
        self.title = title
        self.completed = completed
        self.due_date = due_date
        self.created_at = datetime.now().isoformat()

class TodoManager:
    def __init__(self):
        self.todos: List[TodoItem] = []
        self.next_id = 1
    
    def add_todo(self, title: str, due_date: Optional[str] = None) -> TodoItem:
        """Add a new todo item"""
        todo = TodoItem(id=self.next_id, title=title, due_date=due_date)
        self.todos.append(todo)
        self.next_id += 1
        return todo
    
    def get_todos(self) -> List[TodoItem]:
        """Get all todos"""
        return self.todos
    
    def get_todo_by_id(self, todo_id: int) -> Optional[TodoItem]:
        """Get a specific todo by ID"""
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def update_todo(self, todo_id: int, title: Optional[str] = None, 
                   completed: Optional[bool] = None, due_date: Optional[str] = None) -> Optional[TodoItem]:
        """Update a todo item"""
        todo = self.get_todo_by_id(todo_id)
        if todo:
            if title is not None:
                todo.title = title
            if completed is not None:
                todo.completed = completed
            if due_date is not None:
                todo.due_date = due_date
        return todo
    
    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo item"""
        original_length = len(self.todos)
        self.todos = [todo for todo in self.todos if todo.id != todo_id]
        return len(self.todos) < original_length
    
    def mark_complete(self, todo_id: int) -> Optional[TodoItem]:
        """Mark a todo as complete"""
        return self.update_todo(todo_id, completed=True)
    
    def mark_incomplete(self, todo_id: int) -> Optional[TodoItem]:
        """Mark a todo as incomplete"""
        return self.update_todo(todo_id, completed=False)
    
    def get_completed_todos(self) -> List[TodoItem]:
        """Get all completed todos"""
        return [todo for todo in self.todos if todo.completed]
    
    def get_pending_todos(self) -> List[TodoItem]:
        """Get all pending todos"""
        return [todo for todo in self.todos if not todo.completed]
    
    def clear_completed(self):
        """Remove all completed todos"""
        self.todos = [todo for todo in self.todos if not todo.completed]
    
    def search_todos(self, query: str) -> List[TodoItem]:
        """Search todos by title"""
        query_lower = query.lower()
        return [todo for todo in self.todos if query_lower in todo.title.lower()]

# Global instance for demo purposes
todo_manager = TodoManager()