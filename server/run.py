import uvicorn

from core.config import config as CONFIG

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=CONFIG.PORT,
        reload=CONFIG.RELOAD,
        # reload_dirs=["server"] if CONFIG.RELOAD else [],
    )
