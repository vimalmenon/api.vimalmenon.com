from pydantic import BaseModel


class VimCommand(BaseModel):
    describe: str
    command: str
    language: str


class UpdateVimCommand(BaseModel):
    id: str
    app: str
    describe: str
    command: str
    language: str
