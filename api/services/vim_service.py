from api.managers.dynamodb.dynamo_db_table import DynamoDbTable
from api.serializers.vim_command import VimCommand, UpdateVimCommand
from api.models.vim_model import VimModel


class VimService:
    dynamodb: DynamoDbTable

    def __init__(self):
        self.dynamodb = DynamoDbTable()

    def get_data(self):
        pass

    def update_data(self, data: UpdateVimCommand):
        return self.dynamodb.update_item(data)

    def add_data(self, data: VimCommand):
        result = self.dynamodb.add_item(data)
        return result["ResponseMetadata"]["HTTPStatusCode"] == 200

    def delete_data(self, id: str):
        result = self.dynamodb.delete_item(id)
        return result["ResponseMetadata"]["HTTPStatusCode"] == 200

    def scan_item(self):
        result = self.dynamodb.get_items()
        return [
            VimModel(
                id=item["id"],
                describe=item["describe"],
                command=item["command"],
                language=item["language"],
            )
            for item in result["Items"]
        ]
