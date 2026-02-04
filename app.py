from datetime import date

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette import status


app = FastAPI()
@app.get("/")
def visit(
        store_name:str,
        year:int,
        month:int,
        day:int,
        sensor_id:int | None
) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content=f'Salut !!{store_name}')


