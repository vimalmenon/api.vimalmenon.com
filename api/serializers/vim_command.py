from pydantic import BaseModel


class VimCommand(BaseModel):
    describe: str
    command: str
    language: str
    tags: list[str]


class UpdateVimCommand(BaseModel):
    id: str
    describe: str
    command: str
    language: str
    tags: list[str]
