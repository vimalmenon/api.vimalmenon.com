from api.managers.dynamodb.dynamo_db_table import DynamoDbTable
from api.serializers.vim_command import DeleteVimCommand


class VimService:
    dynamodb: DynamoDbTable

    def __init__(self):
        self.dynamodb = DynamoDbTable()

    def get_data(self):
        pass

    def update_data(self):
        pass

    def add_data(self):
        pass

    def delete_data(self, data: DeleteVimCommand):
        return self.dynamodb.delete_item(data)

    def scan_item(self):
        return self.dynamodb.get_items()
