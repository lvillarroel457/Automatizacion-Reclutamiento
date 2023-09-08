import json
from flask import Flask, jsonify, render_template, request
from main.adapters.openai_recruiter import OpenAiRecruiter
from main.adapters.file_parser import DocxFileParser
from main.domain.cv import CV
from main.service.standardize_cv_softserve import StandardizeCvSoftServeService

app = Flask(__name__)

recruiter = OpenAiRecruiter()
text_parser = DocxFileParser()
candidate_parser = OpenAiRecruiter()

standardize_cv_service = StandardizeCvSoftServeService(recruiter, text_parser)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/standardize_cv', methods=['POST'])
def standardize_cv():
    candidates_files = request.files.getlist('candidates_contents')
    service_request = {"candidates_contents": candidates_files}
    result = standardize_cv_service.execute(request=service_request)
    formated = json.loads(result)
    print(formated)
    candidates = [CV.from_json(candidate_dict) for candidate_dict in formated['candidates']]
    formatted_cvs = [render_template('template_cv_softserve.html', candidate=candidate) for candidate in candidates]
    return '\n\n'.join(formatted_cvs)

if __name__ == '__main__':
    app.run()
