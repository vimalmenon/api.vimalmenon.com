from api.managers.dynamodb.dynamo_db_table import DynamoDbTable


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

    def delete_data(self, id: str):
        return self.dynamodb.delete_item(id)

    def scan_item(self):
        return self.dynamodb.get_items()
