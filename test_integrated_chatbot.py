"""Test script for the integrated AI Chatbot functionality"""

import asyncio
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent.todo_agent import run_todo_agent

# Set the Cohere API key
os.environ["COHERE_API_KEY"] = "lvtEngtl7zyrJnydMS3G48k5636PFO6ShfeRSiAV"

async def test_integrated_chatbot():
    """Test the integrated chatbot functionality."""
    print("Testing Integrated Todo AI Chatbot...")
    
    # Use a simulated user ID
    test_user_id = "1"  # This would be the authenticated user's ID in the real app

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

    print(f"\n3. Testing task completion:")
    result3 = await run_todo_agent(
        user_message="I finished buying groceries, mark it as completed",
        user_id=test_user_id,
        conversation_id=result1['conversation_id']
    )
    print(f"Response: {result3['response']}")
    print(f"Tool calls: {result3['tool_calls']}")

    print("\nIntegrated chatbot test completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_integrated_chatbot())