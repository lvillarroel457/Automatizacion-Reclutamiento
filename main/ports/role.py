from abc import ABC, abstractmethod

class Role(ABC):

    @abstractmethod
    def parse_role(raw_role):
        pass