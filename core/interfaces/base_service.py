from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def process_data(self, data):
        pass