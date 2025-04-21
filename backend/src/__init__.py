from fastapi import FastAPI
from src.endpoints.generate_data import generate_data_router

version = "v1"
app = FastAPI(version=version)
app.include_router(generate_data_router, prefix=f"/api/{version}/generate-data")
