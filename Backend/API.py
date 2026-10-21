import os
import secrets
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

p1ID = os.getenv("partner1_code")
p2ID = os.getenv("partner2_code")

accepted_users = ["ashtyn", "rusty"]

def generate_client_auth():
    secret = secrets.token_bytes(32)
    
    return secret

class User:
    
    def __init__(self, username: str):

        username = username.lower()

        self.username = username
        self.secret = generate_client_auth()
        self.activated = True
        
        if username == "ashtyn":
            self.pid = p1ID
        elif username == "rusty":
            self.pid = p2ID
        else:
            print("Username not seen.")
            raise ValueError("Username not found.")

@app.get("/test")
def say_hi():
    return {"Hi!"}

@app.get("/create-user")
def create_user(username: str):
    
    username = username.lower() # Lowercases this because I'm an actual idiot.
    
    if username not in accepted_users:
        return {f"{username} is not valid!"}
    elif username in accepted_users:
        user = User(username)
        return {f"{username} is valid! You're not a moron!"}
    else:
        return {"Debug this error you dickhead."}
