from fastapi import FastAPI, Depends, HTTPException

from corona_travel_server import __version__
from corona_travel_server.config import Settings, get_settings
from corona_travel_server.models import Marker, Markers
from corona_travel_server.db_connect import get_db


app = FastAPI(
    title=get_settings().app_name,
    version=__version__,
)


@app.on_event("startup")
def startup_event(settings: Settings = Depends(get_settings)):
    # add check that db and collections exist
    pass


@app.get("/test")
async def test(settings: Settings = Depends(get_settings)):
    return {
        "name": settings.app_name,
        "version": __version__,
    }


@app.get("/markers", response_model=Markers)
async def get_markers(settings: Settings = Depends(get_settings)):
    db = get_db(settings.mongo_url)
    if 'place' not in db.list_collection_names():
        print('Collection not found')
        raise HTTPException(
            status_code=500,
            detail="Collection not found",
        )
    marker_collection = db.place
    markers = marker_collection.find({})
    res = []
    for m in markers:
        try:
            res.append(Marker(**m))
        except Exception as e:
            print(str(e))
    return res
