from fastapi import APIRouter

from api.managers.dynamodb.dynamo_db_table import DynamoDbTable


route = APIRouter()


@route.get("/", tags=["vim"])
async def get_vim_data():
    return DynamoDbTable().get_creation_data()
