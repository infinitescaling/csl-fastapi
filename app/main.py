from fastapi import FastAPI
import requests
from .helpers.get_twitch_auth import load_creds
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/live")
async def check_live():
    creds = load_creds()
    client_id = creds["client_id"]
    client_secret = creds["client_secret"]
    
    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    x = requests.post(url, json = payload);

