from abc import ABC, abstractmethod


class TableAbstract(ABC):
    @abstractmethod
    def get_creation_data(self):
        pass
