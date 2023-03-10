from fastapi import APIRouter

from api.routes import emotes, exceptions


def setup(router: APIRouter):
    emotes.setup(router)
