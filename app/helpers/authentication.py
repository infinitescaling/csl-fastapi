import os

def load_creds(cred_type: str):

    try:
        client_id = os.getenv('twitch_client_id')
        client_secret = os.getenv('twitch_client_secret')
    
    except:
        with open(f"etc/{cred_type}/client_id/value") as f:
            client_id = f.read()

        with open(f"etc/{cred_type}/client_secret/value") as f:
            client_secret = f.read()

    return {
        "client_id": client_id,
        "client_secret": client_secret
    }