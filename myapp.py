import requests
import json

URL = "http://127.0.0.1:8000/empcreate/"

data = {
    'name': 'Sahil', 'emp_id': 3, 'salary': 25000, 'city': 'Kolhapur'
}
jason_data = json.dumps(data)
r = requests.post(url=URL, data=jason_data)
data = r.json()
print(data)
