from pymongo import MongoClient
from pydantic import AnyUrl


def get_db(url: AnyUrl):
    # check that connected
    try:
        client = MongoClient(url, serverSelectionTimeoutMS = 5000)
        client.server_info()
        db = client.corona_travel
        # check auth
        # docker compose env
        return db
    except:
        print('Connection error')
