import uvicorn

from configs.settings import settings
from internal.app.app import create_app as backend_app

app = backend_app()


if __name__ == "__main__":
    # development server
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True)
