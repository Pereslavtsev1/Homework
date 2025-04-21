from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.endpoints.generate_data import generate_data_router

version = "v1"
app = FastAPI(version=version)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(generate_data_router, prefix=f"/api/{version}/generate-data")
