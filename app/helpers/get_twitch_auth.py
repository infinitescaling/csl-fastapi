import sys
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