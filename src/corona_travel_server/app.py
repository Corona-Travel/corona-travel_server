from fastapi import FastAPI

from corona_travel_server import __version__

app = FastAPI()


@app.get("/test")
async def test():
    return {"version": __version__}
