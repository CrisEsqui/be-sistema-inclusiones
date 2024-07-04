from fastapi import FastAPI
from api import init_api

def create_app() -> FastAPI:

    app = FastAPI(docs_url='/')

    init_api(app)

    return app
