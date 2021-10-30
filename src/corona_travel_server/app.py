from fastapi import FastAPI, Depends

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
    marker_collection = db.place
    markers = marker_collection.find({})
    # check that this works
    res = []
    for m in markers:
        res.append(Marker(**m))
    return res
