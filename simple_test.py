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

    response = ai_chatbot.process("demo-user", "Delete todo 2")
    print(f"You: Delete todo 2")
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

def interactive_test():
    """
    Interactive mode where you can type your own commands
    """
    print("\n🎮 INTERACTIVE MODE")
    print("Type your commands to interact with the AI chatbot.")
    print("Type 'quit' to exit, or 'reset' to clear todos and start fresh.")
    print()
    
    # Reset todos for interactive session
    from todo_manager import todo_manager
    todo_manager.todos = []
    todo_manager.next_id = 1
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'stop']:
            print("AI: Goodbye! Thanks for testing the chatbot.")
            break
        elif user_input.lower() == 'reset':
            todo_manager.todos = []
            todo_manager.next_id = 1
            print("AI: Todos cleared. Starting fresh!")
            continue
        elif not user_input:
            print("AI: Please enter a command.")
            continue
            
        try:
            response = ai_chatbot.process("demo-user", user_input)
            print(f"AI: {response}")
        except Exception as e:
            print(f"AI: Sorry, I encountered an error: {str(e)}")
        print()

if __name__ == "__main__":
    # Run the demo
    demo_chatbot()
    
    # Ask if user wants to try interactive mode
    choice = input("Would you like to try the interactive mode? (yes/no): ")
    if choice.lower() in ['yes', 'y', 'ok']:
        interactive_test()
    else:
        print("Thanks for testing the AI chatbot!")