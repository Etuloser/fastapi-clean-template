from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from configs import settings


def create_app() -> FastAPI:
    app = FastAPI()
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                str(origin)
                for origin in settings.BACKEND_CORS_ORIGINS
            ],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
    return app
