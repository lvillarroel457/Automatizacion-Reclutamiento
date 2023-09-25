from flask import Flask, jsonify, render_template, request
from main.adapters.cv_docx_formatter import DOCXCVFormatter
from main.adapters.openai_recruiter import OpenAiRecruiter
from main.adapters.file_readers import AllFileParser #DocxFileParser
from main.service.standardize_cv_softserve import StandardizeCvSoftServeService
import concurrent.futures
import os
from flask import send_from_directory


app = Flask(__name__)

recruiter = OpenAiRecruiter()
text_parser = AllFileParser() #DocxFileParser()
candidate_parser = OpenAiRecruiter()
formatter = DOCXCVFormatter()

@app.route('/')
def index():
    return render_template('index.html')

def process_cv(raw_cv_file):
    service = StandardizeCvSoftServeService(recruiter, text_parser, formatter)
    service_request = {"raw_cv_file": raw_cv_file}
    output_file = service.execute(request=service_request)
    return output_file

@app.route('/standardize_cv', methods=['POST'])
def standardize_cv():
    output_files = []
    # retrieve list of raw source cv files
    candidates_files = request.files.getlist('candidates_contents')

    # process files in parallel using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(process_cv, candidates_files)
        output_files.extend(results)

    return render_template('results.html', output_files=output_files)

@app.route('/output_files/<filename>')
def download_file(filename):
    current_directory = os.getcwd()
    return send_from_directory(current_directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
