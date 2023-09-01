from abc import ABC, abstractmethod

from main.domain.candidate import Candidate

class CandidateParser(ABC):

    @abstractmethod
    def parse(candidates_contents):
        pass
