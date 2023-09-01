from main.ports.job_matcher import JobMatcher
from main.ports.text_parser import TextParser
from main.ports.candidate_parser import CandidateParser

class BestNMatchesService:

    def __init__(self, job_matcher: JobMatcher, text_parser: TextParser, candidate_parser: CandidateParser):
        self._job_matcher = job_matcher
        self._text_parser = text_parser
        self._candidate_parser = candidate_parser

    def execute(self, request: dict):
        candidates_contents = self._text_parser.parse(request["candidates_contents"])
        job_position_text = self._text_parser.parse(request["job_post_contents"])
        best_n = request["best_n"]
        result = self._job_matcher.best_n_matches_from_str(candidates=candidates_contents, job_position_text=job_position_text, best_n=best_n)
        return result
