from fastapi import APIRouter


route = APIRouter()


@route.get("/", tags=["links"])
async def get_data():
    pass
