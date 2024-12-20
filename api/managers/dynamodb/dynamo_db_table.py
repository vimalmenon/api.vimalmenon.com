import uuid
from api.managers.dynamodb.table_abstract import TableAbstract
from api.serializers.vim_command import VimCommand
from api.config.env import env
from api.managers.aws.session import Session
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError
from api.exceptions.exception import DbException


class DynamoDbTable(TableAbstract):

    def __init__(self):
        session = Session().get_session()
        dynamodb = session.resource("dynamodb")
        self.table = dynamodb.Table(env.table)

    def get_creation_data(self):
        return self.table.creation_date_time

    def get_items(self):
        try:
            return self.table.scan(FilterExpression=Attr("app").eq("vm#vim"))
        except ClientError:
            raise DbException(detail="Error while quering data")

    def add_item(self, data: VimCommand):
        try:
            return self.table.put_item(
                Item={
                    "id": str(uuid.uuid4()),
                    "app": "vm#vim",
                    "describe": data.describe,
                    "command": data.command,
                    "language": data.language,
                }
            )
        except ClientError:
            raise DbException(detail="Error while deleting data")

    def delete_item(self, id: str):
        try:
            return self.table.delete_item(Key={"id": id, "app": "vm#vim"})
        except ClientError:
            raise DbException(detail="Error while deleting data")

    def update_item(self, data):
        return self.table.update_item(
            Key={
                "id": data.id,
                "app": "vm#vim",
            },
            UpdateExpression="Set #describe = :describe, #command =:command, #language = :language",
            ExpressionAttributeValues={
                ":describe": data.describe,
                ":command": data.command,
                ":language": data.language,
            },
            ExpressionAttributeNames={
                "#describe": "describe",
                "#command": "command",
                "#language": "langauge",
            },
        )

    def scan_items(self):
        return self.table.scan()
