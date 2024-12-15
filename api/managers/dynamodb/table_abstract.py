from abc import ABC, abstractmethod


class TableAbstract(ABC):
    @abstractmethod
    def get_creation_data(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def add_item(self, data):
        pass

    @abstractmethod
    def delete_item(self, data):
        pass

    @abstractmethod
    def update_item(self, data):
        pass
