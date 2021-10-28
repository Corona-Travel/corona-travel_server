from fastapi import FastAPI, Depends

from corona_travel_server import __version__
from corona_travel_server.config import Settings, get_settings

app = FastAPI()


@app.get("/test")
async def test(settings: Settings = Depends(get_settings)):
    return {
        "name": settings.app_name,
        "version": __version__,
    }
