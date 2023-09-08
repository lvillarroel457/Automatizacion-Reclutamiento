from abc import ABC, abstractmethod
from typing import List

class Recruiter(ABC):
    @abstractmethod
    def parse_candidate(self, candidates_contents: List[str]):
        pass
