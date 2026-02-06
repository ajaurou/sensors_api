import logging

from datetime import date
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette import status
from fake_data_app import create_app

store_dict = create_app()
app = FastAPI()
@app.get("/")
def visit(
        store_name:str,
        year:int,
        month:int,
        day:int,
        sensor_id:int | None = None
) -> JSONResponse:

    # Check the store name
    if store_name not in store_dict.keys():
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"Store {store_name} not found")


    try:
        queried_date = date(year, month, day)
    except ValueError as e:
        logging.error(f'Could not cast dat: {e}')
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='Enter a valid date')

    if year < 2019:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No data before 2019")
    elif queried_date > date.today():
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Date is in the future")

    if sensor_id is None:
        visit_counts = store_dict[store_name].get_store_traffic(queried_date)
        return JSONResponse(status_code=status.HTTP_200_OK, content=visit_counts)
    elif sensor_id > 7 or sensor_id < 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='Sensor ID not found or not valid')
    else:
        visit_counts = store_dict[store_name].get_sensor_traffic(sensor_id,
                                                                 queried_date)


    return JSONResponse(status_code=status.HTTP_200_OK, content=f'Salut !!{store_name}')


