from abc import ABC, abstractmethod

class Matcher(ABC):

    @abstractmethod
    def match_candidate(candidate , role):
        pass


class MatchFormatter(ABC):

    @abstractmethod
    def format_match(MatchList, output_file: str):
        pass

    def format_matchtpl(MatchList, output_file: str):
        pass    
