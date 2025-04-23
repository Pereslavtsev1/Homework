from fastapi import APIRouter

from src.services.data_generator_service import DataGeneratorService
from src.utils.DataType import DataType

generate_data_router = APIRouter()


@generate_data_router.get("/")
def handle_generate_data(type: DataType, valid: bool = False):
    return {"content": DataGeneratorService.generate_data(type, valid)}
