import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import lifespan

app = FastAPI(
    lifespan=lifespan.manage_lifespan,
    title="FastAPI Boilerplate",
    openapi_url="/openapi.json"
)

origins = ["localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/', description="Entry page")
def show_main_page():
    logging.debug("Called Main Page")
    return "OK"