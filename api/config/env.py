import os


class Env:
    env = os.getenv("ENV")
    debug = os.getenv("DEBUG", False)
    table = os.getenv("TABLE")


env = Env()
