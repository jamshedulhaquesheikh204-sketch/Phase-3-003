import os
import asyncio
from agent.todo_agent import TodoAgent

async def debug_test():
    # Set the API key directly in the environment for this test
    os.environ["COHERE_API_KEY"] = "lvtEngtl7zyrJnydMS3G48k5636PFO6ShfeRSiAV"

    agent = TodoAgent()

    print("Testing agent with simple message...")
    try:
        result = await agent.run_agent(
            user_message="Say hello",
            user_id="debug-test-user"
        )
        print("Simple message success:", result['response'][:50])
    except Exception as e:
        print(f"Simple message error: {e}")
        import traceback
        traceback.print_exc()

    print("\nTesting agent with task creation message...")
    try:
        result = await agent.run_agent(
            user_message="Add a task to buy groceries including milk and eggs",
            user_id="debug-test-user"
        )
        print("Task creation success:", result['response'][:50])
    except Exception as e:
        print(f"Task creation error: {e}")
        import traceback
        traceback.print_exc()
        # Also try to see what's happening with a simpler task
        print("\nTrying with a simpler task...")
        try:
            result = await agent.run_agent(
                user_message="Add a task: Buy milk",
                user_id="debug-test-user"
            )
            print("Simple task success:", result['response'][:50])
        except Exception as e2:
            print(f"Simple task error: {e2}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(debug_test())