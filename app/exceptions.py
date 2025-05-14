from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


def handle_database_error(error_message: str):
    error_message = error_message.lower()
    if "unique constraint" in error_message:
        return HTTPException(
            status_code=400,
            detail="A resource with the same unique identifier already exists.",
        )
    elif "foreign key constraint" in error_message:
        return HTTPException(
            status_code=400,
            detail="Invalid foreign key reference. Please check related data.",
        )
    else:
        return HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {error_message}"
        )


async def custom_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
