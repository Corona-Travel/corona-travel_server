from fastapi import FastAPI, Depends

from corona_travel_server import __version__
from corona_travel_server.config import Settings, get_settings
from corona_travel_server.models import Markers

app = FastAPI()


@app.get("/test")
async def test(settings: Settings = Depends(get_settings)):
    return {
        "name": settings.app_name,
        "version": __version__,
    }

@app.get("/markers", response_model=Markers)
async def get_markers() -> Markers:
    raise NotImplementedError
