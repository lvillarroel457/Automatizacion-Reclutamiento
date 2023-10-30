from main.ports.file_reader import FileReader
from docx import Document
import csv
import json
from werkzeug.utils import secure_filename
import docx2txt
from PyPDF2 import PdfReader 

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

class DocxFileParser1(FileReader):
    def read(self, source):
        doc = Document(source)
        return ' '.join(paragraph.text for paragraph in doc.paragraphs)

class DocxFileParser2(FileReader): #Mejor
    def read(self, source):
        return docx2txt.process(source) 

        


class PdfFileParser(FileReader):
    def read(self,source):
        doc = PdfReader(source) 
        return  ' '.join(page.extract_text() for page in doc.pages)


class AllFileParser(FileReader):
    def read(self,source):
        filename = secure_filename(source.filename)
        if filename.rsplit('.', 1)[1].lower()=='pdf':
            doc = PdfReader(source)
            return  ' '.join(page.extract_text() for page in doc.pages) 

        elif filename.rsplit('.', 1)[1].lower()=='docx':

            return docx2txt.process(source) 
        else:
            print('El formato del archivo no es compatible')
            return None               
