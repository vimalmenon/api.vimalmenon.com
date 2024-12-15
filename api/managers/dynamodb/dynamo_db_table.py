import boto3
import uuid
from api.managers.dynamodb.table_abstract import TableAbstract
from api.serializers.vim_command import VimCommand, DeleteVimCommand
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
        return self.table.put_item(
            Item={
                "id": str(uuid.uuid4()),
                "app": "vm#vim",
                "describe": data.describe,
                "command": data.command,
                "language": data.language,
            }
        )

    def delete_item(self, data: DeleteVimCommand):
        return self.table.delete_item(Key={"id": data.id, "app": data.app})

    def update_item(self, data):
        pass
