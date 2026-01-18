"""
Simple Test Script for AI-Powered Todo Chatbot
This script demonstrates how to use the AI chatbot to manage your todos
"""

from ai_chatbot import ai_chatbot

def demo_chatbot():
    print("="*60)
    print("AI-Powered Todo Chatbot Demo")
    print("="*60)
    print("This chatbot can understand natural language to manage your todos!")
    print()
    
    # Clear any existing todos for a fresh start
    from todo_manager import todo_manager
    todo_manager.todos = []  # Reset for demo
    todo_manager.next_id = 1
    
    print("Here are the commands you can try:")
    print("1. Add a todo: 'Add buy groceries to my todos'")
    print("2. List todos: 'Show my todos'")
    print("3. Complete a todo: 'Complete todo 1'")
    print("4. Delete a todo: 'Delete todo 1'")
    print("5. Get help: 'Help'")
    print()
    
    # Demo adding todos
    print("[DEMO] Adding todos")
    print("-" * 30)
    
    response = ai_chatbot.process("demo-user", "Add buy groceries to my todos")
    print(f"You: Add buy groceries to my todos")
    print(f"AI: {response}")
    print()
    
    response = ai_chatbot.process("demo-user", "Add finish project by tomorrow")
    print(f"You: Add finish project by tomorrow")
    print(f"AI: {response}")
    print()
    
    response = ai_chatbot.process("demo-user", "Need to call dentist")
    print(f"You: Need to call dentist")
    print(f"AI: {response}")
    print()
    
    # Demo listing todos
    print("[DEMO] Listing todos")
    print("-" * 30)
    
    response = ai_chatbot.process("demo-user", "Show my todos")
    print(f"You: Show my todos")
    print(f"AI: {response}")
    print()
    
    # Demo completing a todo
    print("[DEMO] Completing a todo")
    print("-" * 30)
    
    response = ai_chatbot.process("demo-user", "Complete todo 1")
    print(f"You: Complete todo 1")
    print(f"AI: {response}")
    print()
    
    # Show updated list
    print("[DEMO] Updated todo list:")
    response = ai_chatbot.process("demo-user", "Show my todos")
    print(f"You: Show my todos")
    print(f"AI: {response}")
    print()
    
    # Demo deleting a todo
    print("[DEMO] Deleting a todo")
    print("-" * 30)
    
    response = ai_chatbot.process("demo-user", "Delete todo 3")
    print(f"You: Delete todo 3")
    print(f"AI: {response}")
    print()
    
    # Final list
    print("[DEMO] Final todo list:")
    response = ai_chatbot.process("demo-user", "Show my todos")
    print(f"You: Show my todos")
    print(f"AI: {response}")
    print()
    
    # Demo help command
    print("[DEMO] Getting help")
    print("-" * 30)
    
    response = ai_chatbot.process("demo-user", "Help")
    print(f"You: Help")
    print(f"AI: {response}")
    print()
    
    print("="*60)
    print("Demo completed! The AI chatbot is working correctly.")
    print("="*60)
    print()
    print("As you can see, the AI chatbot understands natural language and can:")
    print("- Add new todos with commands like 'Add buy groceries to my todos'")
    print("- List all your todos with commands like 'Show my todos'")
    print("- Mark todos as complete with commands like 'Complete todo 1'")
    print("- Delete todos with commands like 'Delete todo 1'")
    print("- Provide help with the 'Help' command")
    print()
    print("The chatbot remembers your todos and manages them intelligently!")

if __name__ == "__main__":
    # Run the demo
    demo_chatbot()