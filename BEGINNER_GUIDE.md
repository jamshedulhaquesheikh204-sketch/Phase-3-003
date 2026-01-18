# Guide to Using the AI-Powered Todo Chatbot

## What is this?
The AI-powered Todo Chatbot is a smart assistant that helps you manage your tasks using natural language. Instead of clicking buttons or filling forms, you can just type what you want to do in plain English.

## How to Use the Chatbot

### 1. Adding Todos
To add a new task, simply tell the chatbot what you want to add:
- "Add buy groceries to my todos"
- "I need to call the doctor"
- "Create a task to finish the report"
- "Put workout in my todo list"

### 2. Viewing Your Todos
To see all your tasks:
- "Show my todos"
- "List my tasks"
- "What are my current todos?"
- "Show me my todo list"

### 3. Completing Todos
To mark a task as done:
- "Complete todo 1" (if you know the ID number)
- "Mark buy groceries as done"
- "Finish the workout task"
- "Complete the first task"

### 4. Deleting Todos
To remove a task:
- "Delete todo 1" (if you know the ID number)
- "Remove buy groceries"
- "Delete the workout task"
- "Cancel the first task"

### 5. Getting Help
To see all available commands:
- "Help"
- "What can you do?"
- "Show me commands"

## Example Conversations

Here are some examples of how you can talk to the chatbot:

```
You: Add buy milk to my todos
AI: Added 'buy milk' to your todos. Todo ID: 1

You: Show my todos
AI: You have 1 pending todo(s):
  - [1] buy milk

You: Add finish project by Friday
AI: Added 'finish project' to your todos with due date Friday. Todo ID: 2

You: Show my todos
AI: You have 2 pending todo(s):
  - [1] buy milk
  - [2] finish project (due: Friday)

You: Complete todo 1
AI: Marked 'buy milk' as complete!

You: Show my todos
AI: You have 1 pending todo(s):
  - [2] finish project (due: Friday)

You have completed 1 todo(s):
  - [X] buy milk
```

## Tips for Beginners

1. **Be clear**: The clearer your command, the better the chatbot understands
2. **Use simple language**: Speak naturally, like you're talking to a friend
3. **Remember IDs**: When you add a task, note its ID number for easy reference later
4. **Ask for help**: If you're unsure, just type "Help"

## Behind the Scenes

The chatbot uses artificial intelligence to understand what you're asking. It recognizes patterns in your language and translates them into actions like adding, listing, completing, or deleting tasks.

## Try It Yourself!

You can test the chatbot by running the following Python code:

```python
from ai_chatbot import ai_chatbot

# Process a message
response = ai_chatbot.process("demo-user", "Add learn Python to my todos")
print(response)  # Will print: Added 'learn Python' to your todos. Todo ID: 1
```

Or you can use it through the web interface if you start the server:

```bash
uvicorn main:app --reload
```

Then visit your web app and use the chat interface!

## Troubleshooting

- If the chatbot doesn't understand your command, try rephrasing it
- Make sure you're using the correct demo token ("demo-token") when testing through the API
- If you get an error, check that all the required files are in place (ai_chatbot.py, todo_manager.py, etc.)

Enjoy using your AI-powered todo assistant!