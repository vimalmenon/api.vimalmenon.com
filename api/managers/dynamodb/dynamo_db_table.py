import boto3
from api.managers.dynamodb.table_abstract import TableAbstract
from api.config.env import env

dynamodb = boto3.resource("dynamodb")


class DynamoDbTable(TableAbstract):
    def __init__(self):
        self.table = dynamodb.Table(env.table)

    def get_creation_data(self):
        return self.table.creation_date_time
