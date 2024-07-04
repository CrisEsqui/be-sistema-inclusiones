from fastapi import FastAPI
from api.routers import campus_router

def include_routers(app: FastAPI):

    app.include_router(
        router=campus_router.router,
        prefix='/campus',
        tags=['Campus']
    )