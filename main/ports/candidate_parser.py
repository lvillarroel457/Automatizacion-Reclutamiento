from abc import ABC, abstractmethod

class CandidateParser(ABC):

    @abstractmethod
    def parse(candidates_contents):
        pass
