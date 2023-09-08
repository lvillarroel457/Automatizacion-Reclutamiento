from main.domain.cv import CV
from main.ports.recruiter import Recruiter
from main.ports.file_reader import FileReader
from main.ports.cv_formatter import CVFormatter
from uuid import uuid4
import os
import re
import json


class StandardizeCvSoftServeService:

    def __init__(self, recruiter: Recruiter, text_parser: FileReader, cv_formatter: CVFormatter):
        self._recruiter = recruiter
        self._text_parser = text_parser
        self._cv_formatter = cv_formatter

    def execute(self, request: dict):
        #read raw cv document content into a string
        raw_cv_str = self._text_parser.read(request["raw_cv_file"])

        #ask the recruiter to create a cv json from the raw cv string
        parsed_json_str = self._recruiter.parse_candidate(raw_cv_str)
        
        json_dict = json.loads(parsed_json_str)

        #creates cv object from the recruiter results parsed_json_str
        cv =  CV.from_json(json_dict["candidates"][0])

        #creates output file name
        extension = self._cv_formatter.get_extension()
        file_name = str(uuid4()) + extension
        print(f"filename: {file_name}")

        #creates output file
        self._cv_formatter.format(cv, file_name)

        return file_name
