import os


class Env:
    env = os.getenv("ENV")
    debug = os.getenv("DEBUG", False)


env = Env()
