from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def custom_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        content={"detail": exc.detail},
        status_code=exc.status_code
    )
