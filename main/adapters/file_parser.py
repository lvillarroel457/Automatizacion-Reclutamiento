from main.ports.text_parser import TextParser
from docx import Document
import csv
import json

class TxtFileParser(TextParser):
    def parse(self, source):
        return [open(file_path, 'r', encoding='utf-8').read() for file_path in source]

class CsvFileParser(TextParser):
    def parse(self, source):
        results = []
        for file_path in source:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = [row for row in reader]
                results.append(rows)
        return results

class JsonFileParser(TextParser):
    def parse(self, source):
        return [json.load(open(file_path, 'r', encoding='utf-8')) for file_path in source]

class DocxFileParser(TextParser):
    def parse(self, source):
        return [' '.join(paragraph.text for paragraph in Document(file_path).paragraphs) for file_path in source]
