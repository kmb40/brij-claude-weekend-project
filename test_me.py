# test_me.py

import os
import requests

API_KEY = "sk-abc123secret"
DB_PASSWORD = "supersecret"

def get_user(id):
    r = requests.get("https://api.example.com/users/" + str(id))
    data = r.json()
    return data

def calculate(a, b, operation):
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "divide":
        return a / b  # potential division by zero

def process_users(user_list):
    results = []
    for u in user_list:
        x = get_user(u)
        results.append(x)
        print("processed:", x)
    return results

def reallylongfunctionthatdoestoomanyThings(data, config, user_id, flag1, flag2):
    result = []
    for item in data:
        if flag1:
            item = item.strip()
        if flag2:
            item = item.upper()
        if config.get("validate"):
            if len(item) == 0:
                continue
        result.append(item)
    user = get_user(user_id)
    print(user)
    return result, user