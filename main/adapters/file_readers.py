from main.ports.file_reader import FileReader
from docx import Document
import csv
import json

class TxtFileParser(FileReader):
    def read(self, source):
        with open(source, 'r', encoding='utf-8') as file:
            return file.read()

class CsvFileParser(FileReader):
    def read(self, source):
        with open(source, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row for row in reader]

class JsonFileParser(FileReader):
    def read(self, source):
        with open(source, 'r', encoding='utf-8') as file:
            return json.load(file)

class DocxFileParser(FileReader):
    def read(self, source):
        doc = Document(source)
        return ' '.join(paragraph.text for paragraph in doc.paragraphs)
