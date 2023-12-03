from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import requests
# from .helpers.get_twitch_auth import get_twitch_auth
from .routers import get_live

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

# include routers
app.include_router(get_live.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}



# @app.get("/live")
# async def check_live(username: str):
#     twitch_auth = get_twitch_auth()
#     access_token = twitch_auth["access_token"]
#     client_id = twitch_auth["client_id"]
#     print(f"access_token: {access_token}")
#     print(f"client_id: {client_id}")
    
#     url = "https://api.twitch.tv/helix/streams?user_login=" + username
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Client-Id": client_id,
#         "Access-Control-Allow-Origin": "*",
#     }
#     print(f"headers: {headers}")
#     response = requests.get(url, headers=headers)
#     response_json = response.json()
#     print(response.status_code)
#     if response.status_code != 200  or not response_json["data"]:
#         return False
#     print(f"response_json: {response_json}")
#     # if response_json["data"]:
#     live_status = response_json["data"][0]["type"]
#     if live_status == "live":
#         return True
#     return "False"