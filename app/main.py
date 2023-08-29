from __init__ import (
    __version__,
    __title__,
    static_directory,
    static_mount,
)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import layout
from utils.fastapi_helpers import lifespan
import uvicorn

app = FastAPI(title=__title__, version=__version__, lifespan=lifespan)
app.mount(static_mount, StaticFiles(directory=static_directory))
app.include_router(layout.router)


def start_app():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start_app()
