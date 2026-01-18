"""Test script for Todo AI Chatbot functionality with environment variable"""

import asyncio
import uuid
import os
from agent.todo_agent import run_todo_agent

# Set the Cohere API key
os.environ["COHERE_API_KEY"] = "lvtEngtl7zyrJnydMS3G48k5636PFO6ShfeRSiAV"

async def test_chatbot():
    """Test the chatbot functionality."""
    print("Testing Todo AI Chatbot...")

    # Generate a test user ID
    test_user_id = str(uuid.uuid4())

    try:
        print(f"\n1. Testing task creation:")
        result1 = await run_todo_agent(
            user_message="I need to buy groceries today",
            user_id=test_user_id
        )
        print(f"Response: {result1['response']}")
        print(f"Tool calls: {result1['tool_calls']}")

        print(f"\n2. Testing task listing:")
        result2 = await run_todo_agent(
            user_message="What tasks do I have?",
            user_id=test_user_id,
            conversation_id=result1['conversation_id']
        )
        print(f"Response: {result2['response']}")

        print("\nChatbot test completed successfully!")
    except Exception as e:
        print(f"Error during chatbot test: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_chatbot())