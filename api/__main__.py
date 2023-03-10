import uvicorn as uvicorn
from fastapi import FastAPI

from api import routes


def main():
    app = FastAPI()
    routes.setup(app.router)
    routes.exceptions.setup(app)

    return app


def run():
    uvicorn.run("api:main", factory=True, reload=True)


if __name__ == "__main__":
    run()
