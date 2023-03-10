from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse


async def not_implemented_handler(request: Request, exc: NotImplementedError):
    return JSONResponse(
        status_code=500,
        content={"message": f"Not implemented"},
    )


def setup(app: FastAPI):
    app.add_exception_handler(NotImplementedError, not_implemented_handler)
