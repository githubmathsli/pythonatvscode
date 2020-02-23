import requests

r = requests.get("http://web.wahyan.edu.hk")

print(r.status_code)
print(r.text)
print(r.ok)
