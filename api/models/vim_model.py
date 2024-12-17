from dataclasses import dataclass


@dataclass
class VimModel:
    describe: str
    command: str
    language: str
