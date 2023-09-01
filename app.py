import json
from flask import Flask, jsonify, render_template, request
from main.adapters.openai_job_matcher import OpenAiJobMatcher
from main.adapters.file_parser import DocxFileParser
from main.domain.candidate import Candidate
from main.domain.cv import CV
from main.service.standardize_cv import StandardizeCvService
from main.service.best_n_matches import BestNMatchesService
from main.service.standardize_cv_softserve import StandardizeCvSoftServeService

app = Flask(__name__)

job_matcher = OpenAiJobMatcher()
text_parser = DocxFileParser()
candidate_parser = OpenAiJobMatcher()

standardize_cv_service = StandardizeCvSoftServeService(job_matcher, text_parser, candidate_parser)
# standardize_cv_service = StandardizeCvService(job_matcher, text_parser, candidate_parser)
best_n_service = BestNMatchesService(job_matcher, text_parser, candidate_parser)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/standardize_cv', methods=['POST'])
# def standardize_cv():
#     candidates_files = request.files.getlist('candidates_contents')
#     service_request = {"candidates_contents": candidates_files}
#     result = standardize_cv_service.execute(request=service_request)
#     formated = json.loads(result)
#     candidates = [Candidate.from_json(candidate_dict) for candidate_dict in formated['candidates']]
#     formatted_cvs = [render_template('cv_template.html', candidate=candidate) for candidate in candidates]
#     return '\n\n'.join(formatted_cvs)

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

@app.route('/best_n', methods=['POST'])
def best_n():
    candidates_files = request.files.getlist('candidates_contents')
    job_post_file = request.files.getlist('job_post_contents')
    service_request = {
        "candidates_contents": candidates_files,
        "job_post_contents": job_post_file,
        "best_n": 3}
    result = best_n_service.execute(request=service_request)
    print(result)

    return render_template('match_report.html', candidate=result)

if __name__ == '__main__':
    app.run()
