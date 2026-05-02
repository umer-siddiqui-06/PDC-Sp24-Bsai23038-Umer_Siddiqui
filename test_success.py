import requests
import threading

URL = "http://127.0.0.1:8000/generate"

def send_request(i):
    print(f"Request {i} sent")
    
    try:
        res = requests.post(URL, json={"prompt": f"Hello {i}"})
        print(f"Response {i}: {res.json()}")
    except Exception as e:
        print(f"Request {i} failed: {e}")


# simulate concurrent users (same as test_fail)
threads = []

for i in range(5):
    t = threading.Thread(target=send_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()