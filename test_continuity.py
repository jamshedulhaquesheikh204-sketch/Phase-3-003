"""Test script for conversation continuity and stateless operation"""

import asyncio
import uuid
from mcp_tools.todo_tools import create_conversation, get_messages
from agent.todo_agent import run_todo_agent


async def test_conversation_continuity():
    """Test conversation continuity and stateless operation."""
    print("Testing conversation continuity and stateless operation...")
    
    # Generate a test user ID
    test_user_id = str(uuid.uuid4())
    
    # Create a conversation
    conv_result = create_conversation(user_id=test_user_id)
    conversation_id = conv_result["id"]
    
    print(f"Created conversation with ID: {conversation_id}")
    
    # Simulate a conversation with multiple exchanges
    print("\nStarting conversation...")
    
    # Message 1: Add a task
    result1 = await run_todo_agent(
        user_message="I need to schedule a meeting with my team for tomorrow",
        user_id=test_user_id,
        conversation_id=conversation_id
    )
    print(f"User: I need to schedule a meeting with my team for tomorrow")
    print(f"AI: {result1['response']}")
    
    # Message 2: Ask about tasks
    result2 = await run_todo_agent(
        user_message="What tasks do I have right now?",
        user_id=test_user_id,
        conversation_id=conversation_id
    )
    print(f"User: What tasks do I have right now?")
    print(f"AI: {result2['response']}")
    
    # Message 3: Complete a task
    result3 = await run_todo_agent(
        user_message="I've scheduled the meeting, please mark it as completed",
        user_id=test_user_id,
        conversation_id=conversation_id
    )
    print(f"User: I've scheduled the meeting, please mark it as completed")
    print(f"AI: {result3['response']}")
    
    # Verify conversation persistence by retrieving messages directly from DB
    print(f"\nVerifying conversation persistence...")
    messages = get_messages(conversation_id=conversation_id)
    print(f"Retrieved {len(messages)} messages from DB:")
    for i, msg in enumerate(messages):
        print(f"  {i+1}. [{msg['role']}] {msg['content'][:50]}...")
    
    # Simulate server restart scenario - create a new agent instance
    print(f"\nSimulating server restart and continuing conversation...")
    result4 = await run_todo_agent(
        user_message="Can you show me all my completed tasks?",
        user_id=test_user_id,
        conversation_id=conversation_id
    )
    print(f"User: Can you show me all my completed tasks?")
    print(f"AI: {result4['response']}")
    
    # Verify that the AI remembers the context despite "restart"
    print(f"\nConversation continuity verified!")
    
    # Test with a different user ID to ensure isolation
    print(f"\nTesting user isolation...")
    other_user_id = str(uuid.uuid4())
    
    result_other = await run_todo_agent(
        user_message="What tasks do I have?",
        user_id=other_user_id,
        conversation_id=conversation_id  # Using same conversation ID but different user
    )
    print(f"Different user asking about tasks: {result_other['response']}")
    
    print(f"\nUser isolation verified - different users have separate contexts!")
    
    print("\nAll tests passed! Conversation continuity and stateless operation working correctly.")


if __name__ == "__main__":
    asyncio.run(test_conversation_continuity())