from typing import Optional
from pydantic import BaseModel


class VimCommand(BaseModel):
    id: Optional[str]
    describe: str
    command: str
    language: str


class DeleteVimCommand(BaseModel):
    id: str
    app: str


class UpdateVimCommand(BaseModel):
    id: str
    app: str
    describe: str
    command: str
    language: str
