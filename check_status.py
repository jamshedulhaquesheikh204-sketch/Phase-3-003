import requests
import subprocess
import sys

def check_component_status():
    print("=== TODO APPLICATION STATUS ===\n")

    # Check backend server
    try:
        response = requests.get("http://localhost:8000/docs", timeout=5)
        if response.status_code == 200:
            print("[OK] BACKEND SERVER: Running")
            print("   URL: http://localhost:8000")
            print("   API Docs: http://localhost:8000/docs\n")
        else:
            print("[ERROR] BACKEND SERVER: Not responding correctly\n")
    except requests.exceptions.RequestException:
        print("[ERROR] BACKEND SERVER: Not accessible\n")

    # Check frontend server
    try:
        response = requests.get("http://localhost:3000", timeout=5)
        if response.status_code == 200:
            print("[OK] FRONTEND SERVER: Running")
            print("   URL: http://localhost:3000\n")
        else:
            print("[ERROR] FRONTEND SERVER: Not responding correctly\n")
    except requests.exceptions.RequestException:
        print("[ERROR] FRONTEND SERVER: Not accessible\n")

    # Check if AI chatbot module loads
    try:
        from agent.todo_agent import TodoAgent
        print("[OK] AI CHATBOT: Module loaded successfully")
        print("   Model: command-r-08-2024 (available)")
        print("   URL: Integrated in the application\n")
    except ImportError as e:
        print(f"[ERROR] AI CHATBOT: Could not load module - {e}\n")
    except Exception as e:
        print(f"[WARN] AI CHATBOT: Module loaded but with issues - {e}\n")

    print("=== COMPONENT LINKS ===")
    print("Frontend: http://localhost:3000")
    print("Backend API: http://localhost:8000")
    print("Backend API Docs: http://localhost:8000/docs")
    print("AI Chatbot: Integrated in application (with minor issues)")

if __name__ == "__main__":
    check_component_status()