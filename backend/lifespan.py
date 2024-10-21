import contextlib
import logging

import fastapi


@contextlib.asynccontextmanager
async def manage_lifespan(app: fastapi.FastAPI):
    logging.info("Started FastAPI application.")

    yield

    logging.info("Stopped FastAPI application.")
