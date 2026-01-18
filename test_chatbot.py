"""Test script for Todo AI Chatbot functionality"""

import asyncio
import uuid
from agent.todo_agent import run_todo_agent


async def test_chatbot():
    """Test the chatbot functionality."""
    print("Testing Todo AI Chatbot...")
    
    # Generate a test user ID
    test_user_id = str(uuid.uuid4())
    
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
    
    print(f"\n4. Testing task listing again (should show completed task):")
    result4 = await run_todo_agent(
        user_message="Show me my tasks again",
        user_id=test_user_id,
        conversation_id=result1['conversation_id']
    )
    print(f"Response: {result4['response']}")
    
    print(f"\n5. Testing adding another task:")
    result5 = await run_todo_agent(
        user_message="I need to clean my room tomorrow",
        user_id=test_user_id,
        conversation_id=result1['conversation_id']
    )
    print(f"Response: {result5['response']}")
    print(f"Tool calls: {result5['tool_calls']}")
    
    print(f"\n6. Testing listing pending tasks:")
    result6 = await run_todo_agent(
        user_message="Show me only pending tasks",
        user_id=test_user_id,
        conversation_id=result1['conversation_id']
    )
    print(f"Response: {result6['response']}")
    
    print("\nTest completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_chatbot())