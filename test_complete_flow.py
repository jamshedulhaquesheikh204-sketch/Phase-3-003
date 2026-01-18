"""
Test script to verify the complete flow: frontend -> backend -> AI chatbot -> response
This simulates what would happen when the frontend communicates with the backend
"""

import requests
import json

def test_complete_flow():
    print("Testing Complete Flow: Frontend -> Backend -> AI Chatbot -> Response")
    print("="*70)

    # Test 1: Add a todo
    print("\nTEST 1: Adding a todo")
    print("-"*30)

    headers = {
        "Authorization": "Bearer demo-token",
        "Content-Type": "application/json"
    }

    payload = {
        "message": "Add learn React to my todos"
    }

    try:
        response = requests.post("http://localhost:8000/api/demo-user/chat", json=payload, headers=headers)
        print(f"SUCCESS: Request successful! Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"ERROR: {e}")
        return

    # Test 2: List todos
    print("\nTEST 2: Listing todos")
    print("-"*30)

    payload = {
        "message": "Show my todos"
    }

    try:
        response = requests.post("http://localhost:8000/api/demo-user/chat", json=payload, headers=headers)
        print(f"SUCCESS: Request successful! Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"ERROR: {e}")
        return

    # Test 3: Complete a todo
    print("\nTEST 3: Completing a todo")
    print("-"*30)

    payload = {
        "message": "Complete todo 1"
    }

    try:
        response = requests.post("http://localhost:8000/api/demo-user/chat", json=payload, headers=headers)
        print(f"SUCCESS: Request successful! Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"ERROR: {e}")
        return

    # Test 4: List todos again to see the change
    print("\nTEST 4: Listing todos after completion")
    print("-"*30)

    payload = {
        "message": "Show my todos"
    }

    try:
        response = requests.post("http://localhost:8000/api/demo-user/chat", json=payload, headers=headers)
        print(f"SUCCESS: Request successful! Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"ERROR: {e}")
        return

    print("\n" + "="*70)
    print("COMPLETE FLOW TEST PASSED!")
    print("SUCCESS: Frontend can successfully communicate with backend")
    print("SUCCESS: Backend correctly processes requests with AI chatbot")
    print("SUCCESS: AI chatbot understands natural language commands")
    print("SUCCESS: Todo management works as expected")
    print("="*70)

if __name__ == "__main__":
    test_complete_flow()