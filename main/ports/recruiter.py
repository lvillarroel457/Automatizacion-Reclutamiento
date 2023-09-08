from abc import ABC, abstractmethod
from typing import List

from main.domain.cv import CV

class Recruiter(ABC):
    @abstractmethod
    def parse_candidate(self, candidates_contents: List[str]) -> List[CV]:
        pass
