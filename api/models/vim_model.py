from dataclasses import dataclass


@dataclass
class VimModel:
    id: str
    describe: str
    command: str
    language: str
    tags: list[str]
