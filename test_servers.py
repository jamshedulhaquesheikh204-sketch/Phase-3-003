import time
import requests

print("Waiting for frontend to start...")
time.sleep(10)  # Wait for frontend to start

try:
    response = requests.get("http://localhost:3000", timeout=10)
    if response.status_code == 200:
        print("[OK] FRONTEND SERVER: Running")
        print("URL: http://localhost:3000")
    else:
        print(f"[ERROR] FRONTEND SERVER: Returned status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] FRONTEND SERVER: Not accessible - {e}")

try:
    response = requests.get("http://localhost:8000/docs", timeout=5)
    if response.status_code == 200:
        print("[OK] BACKEND SERVER: Running")
        print("URL: http://localhost:8000")
    else:
        print(f"[ERROR] BACKEND SERVER: Returned status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] BACKEND SERVER: Not accessible - {e}")