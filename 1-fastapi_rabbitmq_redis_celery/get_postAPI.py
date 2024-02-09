import requests

print("=========POST REQUEST=========")
URL = "http://localhost:8000/task"

response = requests.post(url=URL)

json_response = response.json()
task_id = json_response.get("Task id")

print(json_response)
print(task_id)

print("=========GET REQUEST=========")
task_id = "1585ed89-f085-477e-a07b-4792672dde4b"
URL = f"http://localhost:8000/task/{task_id}"

response = requests.get(url=URL)

json_response = response.json()

print(json_response)
