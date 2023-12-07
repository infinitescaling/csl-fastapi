import sys
import requests
from .authentication import load_creds
## This file will pull creds from a mounted drive


def get_twitch_auth():
    creds = load_creds("twitch")
    client_id = creds["client_id"]
    client_secret = creds["client_secret"]
    
    # print(f"client_id: {client_id}")
    # print(f"client_secret: {client_secret}")
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

def get_twitch_info(username: str):
    twitch_auth = get_twitch_auth()
    access_token = twitch_auth["access_token"]
    client_id = twitch_auth["client_id"]
    
    url = "https://api.twitch.tv/helix/streams?user_login=" + username
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": client_id,
        "Access-Control-Allow-Origin": "*",
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    # print(response.status_code)
    if response.status_code != 200  or not response_json["data"]:
        return False
    print(f"response_json: {response_json}")
    # if response_json["data"]:
    live_status = response_json["data"][0]["type"]
    if live_status == "live":
        return {
            "url": f"twitch.tv/{username}"
        }
    return {
            "twitch_live": False
        }