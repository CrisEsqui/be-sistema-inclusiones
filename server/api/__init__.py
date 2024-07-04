from fastapi import FastAPI

from api import root_router
from api.routers import include_routers


def init_api(app: FastAPI):

    # root router, contains health check
    app.include_router(
        router=root_router.router, prefix=f"",
    )

    include_routers(app)