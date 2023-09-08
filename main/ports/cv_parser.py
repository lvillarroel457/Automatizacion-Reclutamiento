from abc import ABC, abstractmethod

class CVParser(ABC):

    @abstractmethod
    def parse(cv_text):
        pass
