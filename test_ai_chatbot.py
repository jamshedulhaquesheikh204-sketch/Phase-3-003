from ai_chatbot import ai_chatbot

def test_ai_chatbot():
    print("Testing AI Chatbot for Todo Management\n")
    
    # Test adding todos
    print("1. Adding todos:")
    response = ai_chatbot.process("demo-user", "Add buy groceries to my todos")
    print(f"   User: Add buy groceries to my todos")
    print(f"   AI: {response}\n")
    
    response = ai_chatbot.process("demo-user", "Add finish project by 12/25/2024")
    print(f"   User: Add finish project by 12/25/2024")
    print(f"   AI: {response}\n")
    
    response = ai_chatbot.process("demo-user", "Need to call dentist")
    print(f"   User: Need to call dentist")
    print(f"   AI: {response}\n")
    
    # Test listing todos
    print("2. Listing todos:")
    response = ai_chatbot.process("demo-user", "Show my todos")
    print(f"   User: Show my todos")
    print(f"   AI: {response}\n")
    
    # Test completing a todo
    print("3. Completing a todo:")
    response = ai_chatbot.process("demo-user", "Complete todo 1")
    print(f"   User: Complete todo 1")
    print(f"   AI: {response}\n")
    
    # Test listing again to see the change
    print("4. Listing todos after completion:")
    response = ai_chatbot.process("demo-user", "Show my todos")
    print(f"   User: Show my todos")
    print(f"   AI: {response}\n")
    
    # Test deleting a todo
    print("5. Deleting a todo:")
    response = ai_chatbot.process("demo-user", "Delete todo 2")
    print(f"   User: Delete todo 2")
    print(f"   AI: {response}\n")
    
    # Final list
    print("6. Final todo list:")
    response = ai_chatbot.process("demo-user", "Show my todos")
    print(f"   User: Show my todos")
    print(f"   AI: {response}\n")

if __name__ == "__main__":
    test_ai_chatbot()