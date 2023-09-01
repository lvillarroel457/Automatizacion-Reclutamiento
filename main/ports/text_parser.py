from abc import ABC, abstractmethod

class TextParser(ABC):

    @abstractmethod
    def parse(source):
        pass
