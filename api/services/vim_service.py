from api.managers.dynamodb.dynamo_db_table import DynamoDbTable
from api.serializers.vim_command import DeleteVimCommand, VimCommand
from api.models.vim_model import VimModel


class VimService:
    dynamodb: DynamoDbTable

    def __init__(self):
        self.dynamodb = DynamoDbTable()

    def get_data(self):
        pass

    def update_data(self):
        pass

    def add_data(self, data: VimCommand):
        return self.dynamodb.add_item(data)

    def delete_data(self, data: DeleteVimCommand):
        return self.dynamodb.delete_item(data)

    def scan_item(self):
        result = self.dynamodb.get_items()
        return [
            VimModel(
                describe=item["describe"],
                command=item["command"],
                language=item["language"],
            )
            for item in result["Items"]
        ]
