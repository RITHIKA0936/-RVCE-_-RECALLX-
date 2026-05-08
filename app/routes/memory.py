from fastapi import APIRouter
from pydantic import BaseModel

from app.memory_store import MemoryStore
from app.response_generator import ResponseGenerator
from app.query_processor import QueryProcessor

router = APIRouter()

memory_store = MemoryStore()

query_processor = QueryProcessor()


class MemoryRequest(BaseModel):
    text: str


@router.post("/add-memory")
def add_memory(request: MemoryRequest):

    memory = memory_store.add_memory(request.text)

    return {
        "message": "Memory added successfully",
        "data": memory
    }


@router.get("/memories")
def get_memories():

    return memory_store.get_all_memories()


@router.post("/search")
def search_memory(request: MemoryRequest):

    try:

        return query_processor.process_query(
            request.text
        )

    except Exception as e:

        return {
            "error": str(e)
        }