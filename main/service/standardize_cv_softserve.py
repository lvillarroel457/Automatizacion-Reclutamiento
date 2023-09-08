from main.ports.job_matcher import Recruiter
from main.ports.text_parser import TextParser
from main.ports.candidate_parser import CandidateParser

class StandardizeCvSoftServeService:

    def __init__(self, recruiter: Recruiter, text_parser: TextParser):
        self._recruiter = recruiter
        self._text_parser = text_parser

    def execute(self, request: dict):
        candidates_contents = self._text_parser.parse(request["candidates_contents"])
        result = self._recruiter.parse_candidate(candidates_contents)
        return result
