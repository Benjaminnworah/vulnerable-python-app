import os
import subprocess

allowed_commands = ["date", "uptime"]

user_input = input("Enter command: ")

if user_input in allowed_commands:
    subprocess.run(user_input.split())
else:
    print("Command not allowed")

password = os.getenv("APP_PASSWORD")

