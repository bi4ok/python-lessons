import json
import requests
import powerset


response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)
with open("json451.json", "w") as json_file:
    json.dump(result, json_file)

user = result[-1]
print(user["userId"])
x = powerset.PowerSet(18, 5)

for i in range(200):
    user = result[i]
    x.put_value(user["userId"])
print(x.len_set())

user = {}
for i in range(200):
    user[result[i]["userId"]] = {"num": 0, "completed": 0}

for j in range(200):
    user[result[j]["userId"]]["num"] += 1
    if result[j]["completed"] is True:
        user[result[j]["userId"]]["completed"] += 1
print(user)
