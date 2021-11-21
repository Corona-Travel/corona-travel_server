from pymongo import MongoClient
from pydantic import AnyUrl


def get_db(url: AnyUrl):
    # check that connected
    try:
        client = MongoClient(url, serverSelectionTimeoutMS = 5000)
        client.server_info()
        if 'corona_travel5' not in client.list_database_names():
            print('Invalid database name')
            return None
        else:
            db = client.corona_travel
            return db
    except:
        print('Connection error')
        return None
