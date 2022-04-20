# Author: Tiago Tamagusko <tamagusko@gmail.com>
from __future__ import annotations

from fastapi import FastAPI

from src.coordinates import router as coordinates
from src.test import router as test

app = FastAPI(
    title='MVP',
    description='Team 01: API to run the MVP backend of the Transatlantic AI Hackathon \
        – Sustainable Supply Chain Deep Hack',
    version='0.1',
)


@app.get('/')
def index():
    return {'data': 'API Running'}


app.include_router(coordinates)
app.include_router(test)
# app.include_router(make_call)
# app.include_router(send_email)
# app.include_router(send_sms)
# app.include_router(monitor)
# app.include_router(optimal_route)
