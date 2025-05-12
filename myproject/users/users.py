# api/users.py

DUMMY_USERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

def get_all_users():
    return DUMMY_USERS

def get_user_by_id(user_id):
    return next((user for user in DUMMY_USERS if user["id"] == user_id), None)
