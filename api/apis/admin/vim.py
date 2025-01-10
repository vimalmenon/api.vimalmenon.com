from fastapi import APIRouter


route = APIRouter()


@route.get("/", tags=["admin_vim"])
async def get_data():
    return {"test": "test"}
