from abc import ABC, abstractmethod
from typing import List

from main.domain.candidate import Candidate

class JobMatcher(ABC):
    @abstractmethod
    def match(self, candidates: List[Candidate], job_position_text: str):
        pass

    @abstractmethod
    def best_n_matches(self, candidates: List[Candidate], job_position_text: str, best_n: int):
        pass

    @abstractmethod
    def match_from_str(self, candidates: List[str], job_position_text: str):
        pass

    @abstractmethod
    def best_n_matches_from_str(self, candidates: List[str], job_position_text: str, best_n: int):
        pass

    @abstractmethod
    def parse(self, candidates_contents: List[str]):
        pass
