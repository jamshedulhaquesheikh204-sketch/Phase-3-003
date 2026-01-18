import requests
import json

# Test the new chat endpoint
BASE_URL = "http://localhost:8000"  # Adjust if your server runs on a different port

def test_chat_endpoint():
    # Headers with demo token
    headers = {
        "Authorization": "Bearer demo-token",
        "Content-Type": "application/json"
    }
    
    # Test adding a todo
    payload = {
        "message": "Add buy milk to my todos"
    }
    
    response = requests.post(f"{BASE_URL}/api/demo-user/chat", json=payload, headers=headers)
    print("Add Todo Response:", response.status_code)
    print(json.dumps(response.json(), indent=2))
    
    # Test listing todos
    payload = {
        "message": "Show my todos"
    }
    
    response = requests.post(f"{BASE_URL}/api/demo-user/chat", json=payload, headers=headers)
    print("\nList Todos Response:", response.status_code)
    print(json.dumps(response.json(), indent=2))
    
    # Test completing a todo
    payload = {
        "message": "Complete todo 1"
    }
    
    response = requests.post(f"{BASE_URL}/api/demo-user/chat", json=payload, headers=headers)
    print("\nComplete Todo Response:", response.status_code)
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    test_chat_endpoint()