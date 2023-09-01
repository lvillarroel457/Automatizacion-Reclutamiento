from main.ports.job_matcher import JobMatcher
from main.ports.text_parser import TextParser
from main.ports.candidate_parser import CandidateParser

class MatchCandidateService:

    def __init__(self, job_matcher: JobMatcher, text_parser: TextParser, candidate_parser: CandidateParser):
        self._job_matcher = job_matcher
        self._text_parser = text_parser
        self._candidate_parser = candidate_parser

    def execute(self, request: dict):
        candidates_contents = self._text_parser.parse(request["candidates_contents"])
        job_position_text = self._text_parser.parse(request["job_position"])
        candidates = self._candidate_parser.parse(candidates_contents)
        result = self._job_matcher.match(candidates=candidates, job_position_text=job_position_text)
        return result
