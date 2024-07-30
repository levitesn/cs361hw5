users = {"admin": "admin"}


def create_user(username, password):
    users[username] = password


def login(username, password):
    if username in users:
        if users[username] == password:
            return 2
        return 1
    return 0
