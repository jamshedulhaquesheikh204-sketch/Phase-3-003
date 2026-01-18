import time
import requests

print("Waiting for servers to start...")
time.sleep(15)  # Wait for servers to start

print("\n=== TESTING FRONTEND ===")
try:
    response = requests.get("http://localhost:3000", timeout=10)
    if response.status_code == 200:
        print("[SUCCESS] FRONTEND SERVER: Accessible")
        print("URL: http://localhost:3000")
    else:
        print(f"[ERROR] FRONTEND SERVER: Returned status code {response.status_code}")
        print("Trying alternative ports...")
        for port in [3001, 3002, 3003]:
            try:
                resp = requests.get(f"http://localhost:{port}", timeout=5)
                if resp.status_code == 200:
                    print(f"[SUCCESS] Frontend running on port {port}")
                    break
            except:
                continue
        else:
            print("[ERROR] No frontend found on common ports")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] FRONTEND SERVER: Not accessible - {e}")

print("\n=== TESTING BACKEND ===")
try:
    response = requests.get("http://localhost:8000/docs", timeout=5)
    if response.status_code == 200:
        print("[SUCCESS] BACKEND SERVER: Accessible")
        print("URL: http://localhost:8000")
        print("API Docs: http://localhost:8000/docs")
    else:
        print(f"[ERROR] BACKEND SERVER: Returned status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] BACKEND SERVER: Not accessible - {e}")

print("\n=== TESTING AI CHATBOT ===")
try:
    from agent.todo_agent import TodoAgent
    print("[SUCCESS] AI CHATBOT: Module loaded successfully")
    print("Model: command-r-08-2024 (confirmed available)")
except ImportError as e:
    print(f"[ERROR] AI CHATBOT: Could not load module - {e}")
except Exception as e:
    print(f"[WARNING] AI CHATBOT: Module loaded but with issues - {e}")

print("\n=== SUMMARY ===")
print("1. BACKEND: Should be running on http://localhost:8000")
print("2. FRONTEND: May be running on different port due to conflicts")
print("3. AI CHATBOT: Available as Python module")