from abc import ABC, abstractmethod

class FileReader(ABC):

    @abstractmethod
    def read(source_file: str):
        pass
