import re
from typing import Dict, List, Tuple
from todo_manager import todo_manager, TodoItem
import json

class AIChatbot:
    def __init__(self):
        # Define patterns for different types of requests
        self.patterns = {
            'add': [
                r'(?:add|create|make|put|set)\s+(?:a\s+|an\s+|the\s+)?(.+?)(?:\s+to\s+my\s+todo(?:s)?|\s+on\s+(?:.+)|\s+by\s+(?:.+)|\s+for\s+(?:.+)|\s+due\s+(?:.+)|$)',
                r'(?:need\s+to|want\s+to|should\s+i|must\s+|have\s+to)\s+(.+?)(?:\s+on\s+(?:.+)|\s+by\s+(?:.+)|\s+for\s+(?:.+)|\s+due\s+(?:.+)|$)',
            ],
            'list': [
                r'(?:list|show|display|see|view|get|fetch|retrieve)\s+(?:my\s+)?(?:all\s+)?(?:of\s+)?(?:my\s+)?todo(?:s)?',
                r'(?:what\'?s|what|show\s+me|display\s+me|list\s+out|tell\s+me)\s+(?:my\s+)?(?:current|existing|pending|active)?\s*todo(?:s)?',
                r'(?:do\s+i\s+have|got|any)\s*(?:pending|active|incomplete)?\s*todo(?:s)?',
            ],
            'complete': [
                r'(?:complete|finish|done|mark\s+as\s+done|check|tick|accomplish)\s+(?:todo\s+|#?(\d+)|the\s+(.+?))',
                r'(?:mark\s+(?:as\s+)?(?:complete|done|finished))\s+(?:todo\s+|#?(\d+)|the\s+(.+?))',
            ],
            'delete': [
                r'(?:delete|remove|erase|clear|get\s+rid\s+of|cancel)\s+(?:todo\s+|#?(\d+)|the\s+(.+?))',
                r'(?:remove\s+(?:from\s+my\s+)?todo(?:s)?)\s+(?:todo\s+|#?(\d+)|the\s+(.+?))',
            ],
            'help': [
                r'(?:help|what\s+can\s+you|how\s+do\s+i|commands|options|features)',
            ]
        }
        
        # Due date patterns
        self.date_patterns = [
            r'on\s+(\d{1,2}[\/\-]\d{1,2}(?:[\/\-]\d{2,4})?)',
            r'by\s+(\d{1,2}[\/\-]\d{1,2}(?:[\/\-]\d{2,4})?)',
            r'due\s+(\d{1,2}[\/\-]\d{1,2}(?:[\/\-]\d{2,4})?)',
            r'for\s+(\d{1,2}[\/\-]\d{1,2}(?:[\/\-]\d{2,4})?)',
        ]

    def extract_date(self, message: str) -> Tuple[str, str]:
        """Extract date from message and return cleaned message"""
        date_match = None
        extracted_date = None
        
        for pattern in self.date_patterns:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                date_match = match
                extracted_date = match.group(1)
                break
        
        if date_match:
            # Remove date part from message
            message = message[:date_match.start()] + message[date_match.end():]
        
        return message.strip(), extracted_date

    def process(self, user_id: str, message: str) -> str:
        """Process a user message and return an appropriate response"""
        message = message.strip().lower()
        
        # Check for different types of requests
        if self._matches_pattern(message, self.patterns['add']):
            return self._handle_add(message)
        elif self._matches_pattern(message, self.patterns['list']):
            return self._handle_list()
        elif self._matches_pattern(message, self.patterns['complete']):
            return self._handle_complete(message)
        elif self._matches_pattern(message, self.patterns['delete']):
            return self._handle_delete(message)
        elif self._matches_pattern(message, self.patterns['help']):
            return self._handle_help()
        else:
            # Try to determine intent based on keywords
            if any(word in message for word in ['add', 'create', 'new', 'need to', 'want to']):
                return self._handle_add(message)
            elif any(word in message for word in ['list', 'show', 'what', 'view', 'see']):
                return self._handle_list()
            elif any(word in message for word in ['complete', 'done', 'finish', 'mark']):
                return self._handle_complete(message)
            elif any(word in message for word in ['delete', 'remove', 'cancel']):
                return self._handle_delete(message)
            else:
                return f"I'm not sure how to help with '{message}'. Try asking me to add, list, complete, or delete a todo."

    def _matches_pattern(self, message: str, patterns: List[str]) -> bool:
        """Check if message matches any of the given patterns"""
        for pattern in patterns:
            if re.search(pattern, message, re.IGNORECASE):
                return True
        return False

    def _extract_todo_id_from_message(self, message: str) -> int:
        """Extract todo ID from message"""
        # Look for number after 'todo' or '#'
        match = re.search(r'(?:todo\s+|#)(\d+)', message, re.IGNORECASE)
        if match:
            return int(match.group(1))
        
        # If no explicit number, try to match by title
        # Find the first todo that contains the key words from the message
        # Remove common words to get the essence of the task
        words = [word for word in message.split() if word not in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'by']]
        if words:
            # Take the first few meaningful words to match against todo titles
            search_text = ' '.join(words[:3])
            for todo in todo_manager.get_todos():
                if search_text.lower() in todo.title.lower():
                    return todo.id
        
        return None

    def _handle_add(self, message: str) -> str:
        """Handle adding a new todo"""
        # Clean up the message to extract the task
        cleaned_message, due_date = self.extract_date(message)
        
        # Extract the task description
        task_match = None
        for pattern in self.patterns['add']:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                task_match = match
                break
        
        if task_match:
            task = task_match.group(1) if task_match.lastindex >= 1 else None
        else:
            # If no match, try to extract the task differently
            # Remove common prefixes
            prefixes = ['add ', 'create ', 'need to ', 'want to ', 'should i ', 'must ', 'have to ']
            task = cleaned_message
            for prefix in prefixes:
                if task.startswith(prefix):
                    task = task[len(prefix):].strip()
                    break
        
        if not task:
            return "I couldn't understand what task you want to add. Please be more specific."
        
        # Clean up the task description
        task = task.strip('.,!?')
        
        # Add the todo
        new_todo = todo_manager.add_todo(task, due_date)
        
        if due_date:
            return f"Added '{new_todo.title}' to your todos with due date {due_date}. Todo ID: {new_todo.id}"
        else:
            return f"Added '{new_todo.title}' to your todos. Todo ID: {new_todo.id}"

    def _handle_list(self) -> str:
        """Handle listing todos"""
        todos = todo_manager.get_todos()
        
        if not todos:
            return "You don't have any todos yet. Add one by saying something like 'Add buy groceries to my todos'."
        
        pending_todos = todo_manager.get_pending_todos()
        completed_todos = todo_manager.get_completed_todos()
        
        response_parts = []
        
        if pending_todos:
            response_parts.append(f"You have {len(pending_todos)} pending todo(s):")
            for todo in pending_todos:
                due_part = f" (due: {todo.due_date})" if todo.due_date else ""
                response_parts.append(f"  - [{todo.id}] {todo.title}{due_part}")
        
        if completed_todos:
            response_parts.append(f"\nYou have completed {len(completed_todos)} todo(s):")
            for todo in completed_todos:
                response_parts.append(f"  - [X] {todo.title}")
        
        return "\n".join(response_parts)

    def _handle_complete(self, message: str) -> str:
        """Handle completing a todo"""
        todo_id = self._extract_todo_id_from_message(message)
        
        if not todo_id:
            # Try to find by title if no ID specified
            # Extract the task name from the message
            task_match = None
            for pattern in self.patterns['complete']:
                match = re.search(pattern, message, re.IGNORECASE)
                if match:
                    # Check if the second group (task name) exists
                    if match.lastindex >= 2:
                        task_match = match.group(2)
                        break
                    elif match.lastindex >= 1 and not match.group(1):  # If first group is empty, it might be the task name
                        task_match = match.group(0)
            
            if task_match:
                # Find the most recently added matching task that's not completed
                task_keywords = task_match.lower().split()
                for todo in reversed(todo_manager.get_pending_todos()):
                    if any(keyword in todo.title.lower() for keyword in task_keywords):
                        todo_id = todo.id
                        break
        
        if todo_id:
            todo = todo_manager.mark_complete(todo_id)
            if todo:
                return f"Marked '{todo.title}' as complete!"
            else:
                return f"I couldn't find a todo with ID {todo_id}."
        else:
            return "I couldn't identify which todo you want to mark as complete. Please specify the todo ID or title."

    def _handle_delete(self, message: str) -> str:
        """Handle deleting a todo"""
        todo_id = self._extract_todo_id_from_message(message)
        
        if not todo_id:
            # Try to find by title if no ID specified
            task_match = None
            for pattern in self.patterns['delete']:
                match = re.search(pattern, message, re.IGNORECASE)
                if match:
                    # Check if the second group (task name) exists
                    if match.lastindex >= 2:
                        task_match = match.group(2)
                        break
                    elif match.lastindex >= 1 and not match.group(1):  # If first group is empty, it might be the task name
                        task_match = match.group(0)
            
            if task_match:
                # Find the most recently added matching task
                task_keywords = task_match.lower().split()
                for todo in reversed(todo_manager.get_todos()):
                    if any(keyword in todo.title.lower() for keyword in task_keywords):
                        todo_id = todo.id
                        break
        
        if todo_id:
            success = todo_manager.delete_todo(todo_id)
            if success:
                return f"Deleted todo with ID {todo_id}."
            else:
                return f"I couldn't find a todo with ID {todo_id}."
        else:
            return "I couldn't identify which todo you want to delete. Please specify the todo ID or title."

    def _handle_help(self) -> str:
        """Provide help information"""
        return """
I can help you manage your todos! Here are the commands you can use:

• Add a new todo: "Add buy groceries to my todos" or "I need to call mom"
• List your todos: "Show my todos" or "What are my current todos?"
• Complete a todo: "Complete todo 1" or "Mark buy groceries as done"
• Delete a todo: "Delete todo 1" or "Remove buy groceries"
• Get help: "Help" or "What can you do?"

Try adding a todo to get started!
"""

# Global instance of the AI chatbot
ai_chatbot = AIChatbot()