from pymongo import MongoClient
from pydantic import AnyUrl


def get_db(url: AnyUrl):
    # check that connected
    client = MongoClient(url)
    db = client.corona_travel
    # check auth
    # docker compose env
    return db
