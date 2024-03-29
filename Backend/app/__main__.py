from contextlib import asynccontextmanager

import uvicorn
from app.boostrap.PropertiesManager import PropertiesManager
from app.middleware.middleware import CheckJwtAuth
from app.routers import artistas, canciones, generos, login, playlists, search, usuarios
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    """Handles the the before and after events of the app start

    Parameters
    ----------
    app : FastAPI
        the app object that is going to be created
    """
    # TODO print init
    app.include_router(playlists.router)
    app.include_router(canciones.router)
    app.include_router(generos.router)
    app.include_router(usuarios.router)
    app.include_router(artistas.router)
    app.include_router(login.router)
    app.include_router(search.router)
    yield
    # teardown app
    # TODO print teardown


app = FastAPI(
    title="SpotifyElectronAPI",
    description="API created with FastAPI Python to serve \
        as backend for Spotify Electron music streaming Desktop App",
    version="1.0.0",
    lifespan=lifespan_handler,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost/",
        "http://localhost:1212",
        "https://localhost:1212/",
        "https://localhost",
        "https://localhost:1212",
        "https://localhost:1212/",
        "http://127.0.0.1:8000/",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE", "PATCH"],
    max_age=3600,
    allow_headers=["*"],
)
app.add_middleware(CheckJwtAuth)


if __name__ == "__main__":
    # TODO reload true condicional
    # TODO meter config lanzar app en config.ini
    uvicorn.run(
        "app.__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=PropertiesManager.is_testing_enviroment(),
    )
