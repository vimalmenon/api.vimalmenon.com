import os


class Env:
    env = os.getenv("ENV")
    debug = os.getenv("DEBUG", False)
    table = os.getenv("TABLE")
    aws_client_id = os.getenv("AWS_CLIENT_ID")
    aws_secret = os.getenv("AWS_SECRET")


env = Env()
