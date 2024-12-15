import boto3
import uuid
from api.managers.dynamodb.table_abstract import TableAbstract
from api.serializers.vim_command import VimCommand
from api.config.env import env

dynamodb = boto3.resource("dynamodb")


class DynamoDbTable(TableAbstract):

    def __init__(self):
        self.table = dynamodb.Table(env.table)

    def get_creation_data(self):
        return self.table.creation_date_time

    def get_items(self):
        return self.table.scan()

    def add_item(self, data: VimCommand):
        result = self.table.put_item(
            Item={
                "id": str(uuid.uuid4()),
                "app": "vm#vim",
                "describe": data.describe,
                "command": data.command,
                "language": data.language,
            }
        )
        print(result)
        breakpoint()
        return ""

    def delete_item(self, id: str):
        return self.table.delete_item(Key={"id": id, "app": "vm#vim"})
