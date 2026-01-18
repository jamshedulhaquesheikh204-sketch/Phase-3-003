import os
import cohere

# Set the API key directly in the environment for this test
os.environ["COHERE_API_KEY"] = "lvtEngtl7zyrJnydMS3G48k5636PFO6ShfeRSiAV"

api_key = os.getenv("COHERE_API_KEY")
client = cohere.Client(api_key)

print("Testing direct Cohere API call...")

# Simple test first
try:
    response = client.chat(
        model="command-r-08-2024",
        message="Say hello",
    )
    print("Simple test successful:", response.text[:50])
except Exception as e:
    print(f"Simple test failed: {e}")
    import traceback
    traceback.print_exc()

# Test with tools
tools = [
    {
        "name": "add_task",
        "description": "Add a new task for the user",
        "parameter_definitions": {
            "user_id": {"type": "string", "description": "The ID of the user"},
            "title": {"type": "string", "description": "The title of the task"},
            "description": {"type": "string", "description": "Optional description of the task"}
        }
    }
]

try:
    response = client.chat(
        model="command-r-08-2024",
        message="Add a task to buy groceries",
        tools=tools
    )
    print("Tool test successful:", response.text[:50])
    if hasattr(response, 'tool_calls') and response.tool_calls:
        print(f"Tool calls detected: {len(response.tool_calls)}")
        for tc in response.tool_calls:
            print(f"  - {tc.name} with params: {tc.parameters}")
except Exception as e:
    print(f"Tool test failed: {e}")
    import traceback
    traceback.print_exc()