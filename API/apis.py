from fastapi import FastAPI
from .user_router import router


def create_app():
    app = FastAPI()
    return app


app = create_app()
app.include_router(router)
