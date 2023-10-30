from main.ports.file_reader import FileReader
from main.ports.matcher import Matcher
from main.ports.matcher import MatchFormatter
from uuid import uuid4


import ast
import json


class MatchCandidatesSoftServeService:

    def __init__(self, file_reader: FileReader, matcher: Matcher, match_formatter: MatchFormatter):
        self._file_reader = file_reader
        self.matcher=matcher
        self.match_formatter=match_formatter

    def execute(self, candidates, role):


        M=[]

        for cv in candidates:
            raw_cv_str = self._file_reader.read(cv)
            raw_match_str = self.matcher.match_candidate(raw_cv_str,role)
            dict_match = ast.literal_eval(raw_match_str)
            M.append(dict_match)

        
        for c in M:
            porcentajes=[int(j[:-1])  for j in list(c.values())[1:]]
            mean=str(round(sum(porcentajes)/len(porcentajes),2))+'%'
            c['Porcentaje Promedio'] = mean

        #Match
        M.sort(key = lambda d: float(d['Porcentaje Promedio'][:-1]), reverse=True)

        #creates output file name
        extension = '.docx'
        file_name = str(uuid4()) + extension

        #creates output file
        self.match_formatter.format_match(M,file_name)

        return file_name
