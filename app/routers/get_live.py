from fastapi import APIRouter
from ..helpers.twitch import get_twitch_info
from ..helpers.youtube import get_youtube_info
from ..helpers.kick import get_kick_info
import requests
router = APIRouter()

@router.get("/live", tags=["live"])
async def check_live(username: str):
    twitch_info = get_twitch_info(username)
    # youtube_info = get_youtube_info(username)
    # kick_info = get_kick_info(username)
    if twitch_info:
        return {
            "platform": "twitch",
            "url": twitch_info["url"]
        }
    # if kick_info:
    #     return {
    #         "platform": "kick",
    #         "url": kick_info["url"]
    #     }
    return False;
    # twitch_auth = get_twitch_auth()
    # access_token = twitch_auth["access_token"]
    # client_id = twitch_auth["client_id"]
    
    # url = "https://api.twitch.tv/helix/streams?user_login=" + username
    # headers = {
    #     "Authorization": f"Bearer {access_token}",
    #     "Client-Id": client_id,
    #     "Access-Control-Allow-Origin": "*",
    # }
    # response = requests.get(url, headers=headers)
    # response_json = response.json()
    # print(response.status_code)
    # if response.status_code != 200  or not response_json["data"]:
    #     return False
    # print(f"response_json: {response_json}")
    # # if response_json["data"]:
    # live_status = response_json["data"][0]["type"]
    # if live_status == "live":
    #     return True
    # return "False"