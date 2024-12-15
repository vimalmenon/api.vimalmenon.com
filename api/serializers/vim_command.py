from typing import Optional
from pydantic import BaseModel


class VimCommand(BaseModel):
    id: Optional[str]
    describe: str
    command: str
    language: str
