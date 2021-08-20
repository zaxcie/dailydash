from abc import ABC, abstractmethod


class Feed(ABC):

    @staticmethod
    @abstractmethod
    def create_items(self):
        pass
