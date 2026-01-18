"""Quick Integration Test for Todo AI Chatbot"""

import asyncio
import uuid
import os
from agent.todo_agent import run_todo_agent


async def quick_test():
    """Quick test to verify the integration works."""
    print("Quick Integration Test for Todo AI Chatbot")
    print("="*50)

    # Set the API key directly to avoid environment variable issues
    os.environ["COHERE_API_KEY"] = "lvtEngtl7zyrJnydMS3G48k5636PFO6ShfeRSiAV"

    # Generate a test user ID
    test_user_id = str(uuid.uuid4())
    print(f"Using test user ID: {test_user_id[:8]}...")

    # Initialize variables to avoid undefined errors
    result1 = None

    print("\n1. Testing task creation:")
    try:
        result1 = await run_todo_agent(
            user_message="Add a task to buy groceries including milk and eggs",
            user_id=test_user_id
        )
        print(f"[SUCCESS] Response: {result1['response'][:60]}...")
        print(f"  Tool calls: {len(result1['tool_calls'])}")
    except Exception as e:
        print(f"[ERROR] {str(e)}")

    print("\n2. Testing task listing:")
    try:
        if result1 is not None:
            result2 = await run_todo_agent(
                user_message="What tasks do I have?",
                user_id=test_user_id,
                conversation_id=result1['conversation_id']
            )
            print(f"[SUCCESS] Response: {result2['response'][:60]}...")
        else:
            print("[ERROR] Cannot proceed with task listing - previous step failed")
    except Exception as e:
        print(f"[ERROR] {str(e)}")

    print("\n3. Testing task completion:")
    try:
        if result1 is not None:
            result3 = await run_todo_agent(
                user_message="Mark the grocery task as completed",
                user_id=test_user_id,
                conversation_id=result1['conversation_id']
            )
            print(f"[SUCCESS] Response: {result3['response'][:60]}...")
        else:
            print("[ERROR] Cannot proceed with task completion - previous step failed")
    except Exception as e:
        print(f"[ERROR] {str(e)}")

    print("\n" + "="*50)
    print("Quick test completed!")


if __name__ == "__main__":
    asyncio.run(quick_test())