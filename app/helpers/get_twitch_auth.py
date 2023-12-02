import sys
import requests
## This file will pull creds from a mounted drive

def load_creds():
    with open("etc/client_id/value") as f:
        client_id = f.read()

    with open("etc/client_secret/value") as f:
        client_secret = f.read()

    return {
        "client_id": client_id,
        "client_secret": client_secret
    }

def get_twitch_auth():
    creds = load_creds()
    client_id = creds["client_id"]
    client_secret = creds["client_secret"]
    
    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, json = payload)
    response_json = response.json()

    access_token = response_json["access_token"]
    return {
        "access_token": access_token,
        "client_id": client_id,
    }