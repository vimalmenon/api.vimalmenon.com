from fastapi import APIRouter

from api.managers.dynamodb.dynamo_db_table import DynamoDbTable
from api.services.vim_service import VimService
from api.serializers.vim_command import VimCommand


route = APIRouter()


@route.get("/", tags=["vim"])
async def get_data():
    return DynamoDbTable().get_items()


@route.post("/", tags=["vim"])
async def post_data(data: VimCommand):
    return DynamoDbTable().add_item(data)


@route.delete("/{id}", tags=["vim"])
async def delete_data(id: str):
    return VimService().delete_data(id)
