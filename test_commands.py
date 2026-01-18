"""
Test script to verify the chatbot commands work correctly
"""

import requests
import json

# Test the specific commands mentioned
BASE_URL = "http://localhost:8000"

def test_commands():
    headers = {
        "Authorization": "Bearer demo-token",
        "Content-Type": "application/json"
    }
    
    print("Testing AI Chatbot Commands")
    print("="*50)
    
    # Test 1: Add a todo first
    print("\n1. Adding a todo...")
    payload = {"message": "Add learn machine learning to my todos"}
    response = requests.post(f"{BASE_URL}/api/demo-user/chat", json=payload, headers=headers)
    print(f"Response: {response.json()}")
    
    # Test 2: Show my todos
    print("\n2. Show my todos...")
    payload = {"message": "Show my todos"}
    response = requests.post(f"{BASE_URL}/api/demo-user/chat", json=payload, headers=headers)
    print(f"Response: {response.json()}")
    
    # Test 3: Complete todo 1
    print("\n3. Complete todo 1...")
    payload = {"message": "Complete todo 1"}
    response = requests.post(f"{BASE_URL}/api/demo-user/chat", json=payload, headers=headers)
    print(f"Response: {response.json()}")
    
    # Test 4: Show completed items
    print("\n4. What have I completed?...")
    payload = {"message": "What have I completed?"}
    response = requests.post(f"{BASE_URL}/api/demo-user/chat", json=payload, headers=headers)
    print(f"Response: {response.json()}")
    
    # Test 5: Delete todo 1 (now completed)
    print("\n5. Delete todo 1...")
    payload = {"message": "Delete todo 1"}
    response = requests.post(f"{BASE_URL}/api/demo-user/chat", json=payload, headers=headers)
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_commands()