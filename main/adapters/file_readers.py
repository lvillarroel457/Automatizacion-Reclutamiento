from main.ports.file_reader import FileReader
from docx import Document
import csv
import json
from werkzeug.utils import secure_filename
from pdfquery import PDFQuery

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


class PdfFileParser(FileReader):
    def read(self,source):
        doc = PDFQuery(source)
        text_elements = doc.pq('LTTextLineHorizontal')
        return  ' '.join(t.text for t in text_elements)


class AllFileParser(FileReader):
    def read(self,source):
        filename = secure_filename(source.filename)
        if filename.rsplit('.', 1)[1].lower()=='pdf':
            doc = PDFQuery(source)
            doc.load()
            text_elements = doc.pq('LTTextLineHorizontal')
            return  ' '.join(t.text for t in text_elements)
        elif filename.rsplit('.', 1)[1].lower()=='docx':
            doc = Document(source)
            return ' '.join(paragraph.text for paragraph in doc.paragraphs) 
        else:
            print('El formato del archivo no es compatible')
            return None               
