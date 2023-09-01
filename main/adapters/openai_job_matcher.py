from main.ports.job_matcher import JobMatcher

import json
import os
import openai

class OpenAiJobMatcher(JobMatcher):

    MATCH_ERROR_MSG = "Error matching: "

    def __init__(self):
        super().__init__()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model_selected = "gpt-3.5-turbo-0613"

    def match(self, candidates, job_position_text: str):
        user_prompt = f"Please match the following candidates with the job position: {job_position_text}. Candidates: {self._candidates_to_string(candidates)}, sort results from best match descending."

        completion = openai.ChatCompletion.create(
            model=self.model_selected,
            messages=[{"role": "user", "content": user_prompt}],
            functions=self._function_description_match_candidate(),
            function_call="auto",
        )

        output = completion.choices[0].message
        match_results = json.loads(output.function_call.arguments)

        return match_results

    def _candidates_to_string(self, candidates):
        candidates_str_list = [str(candidate) for candidate in candidates]
        return ", ".join(candidates_str_list)

    def best_n_matches(self, candidates, job_position_text: str, best_n: int):
        user_prompt = f"Please match the following candidates with the job position: {job_position_text}. Candidates: {self._candidates_to_string(candidates)}, return only the best {best_n} matching candidates."
    
        completion = openai.ChatCompletion.create(
            model=self.model_selected,
            messages=[{"role": "user", "content": user_prompt}],
            functions=self._function_description_match_candidate(),
            function_call="auto",
        )

        output = completion.choices[0].message
        match_results = json.loads(output.function_call.arguments)

        return match_results

    def match_from_str(self, candidates, job_position_text: str):
        user_prompt = f"Please match the following candidates with the job position: {job_position_text}. Candidates: [{', '.join(candidates)}], sort results from best match descending."
        completion = openai.ChatCompletion.create(
            model=self.model_selected,
            messages=[{"role": "user", "content": user_prompt}],
            functions=self._function_description_match_candidate(),
            function_call="auto",
        )

        output = completion.choices[0].message
        match_results = json.loads(output.function_call.arguments)

        return match_results

    def best_n_matches_from_str(self, candidates, job_position_text: str, best_n: int):
        user_prompt = f"Please match the following candidates with the job position: {job_position_text}. Candidates: [{', '.join(candidates)}], return only the best {best_n} matching candidates."
    
        completion = openai.ChatCompletion.create(
            model=self.model_selected,
            messages=[{"role": "user", "content": user_prompt}],
            functions=self._function_description_match_candidate(),
            function_call="auto",
        )

        output = completion.choices[0].message
        match_results = json.loads(output.function_call.arguments)

        return match_results

    def parse(self, candidates_contents):
        try:
            user_prompt = f"Please parse self text: {''.join(candidates_contents)} into a json of candidates"
            completion = openai.ChatCompletion.create(
                model=self.model_selected,
                messages=[{"role": "user", "content": user_prompt}],
                functions=self._function_description_parse_candidate(),
                function_call="auto",
            )

            output = completion.choices[0].message
            candidates = output.function_call.arguments

            return candidates
        except Exception as e:
            print(e.__dict__)

    def parse_softserve(self, candidates_contents):
        try:
            user_prompt = f"Please parse self text: {''.join(candidates_contents)} into a json of cv. Do not add graduation year fields."
            completion = openai.ChatCompletion.create(
                model=self.model_selected,
                messages=[{"role": "user", "content": user_prompt}],
                functions=self._class_cv_description_parse(),
                function_call="auto",
            )

            output = completion.choices[0].message
            candidates = output.function_call.arguments

            return candidates
        except Exception as e:
            print(e.__dict__)

    def _function_description_parse_candidate(self):
        return [
            {
                "name": "parse_candidates",
                "description": "parse candidates from a text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidates": {
                            "type": "array",
                            "description": "List of candidates",
                            "items": {
                                "type": "object",
                                "properties": 
                                {
                                    "candidate_id": {
                                        "type": "string",
                                        "description": "The unique identifier for the candidate."
                                    },
                                    "full_name": {
                                        "type": "string",
                                        "description": "The full name of the candidate."
                                    },
                                    "contact_information": {
                                        "type": "object",
                                        "description": "The contact information of the candidate, including emails, phones, addresses, LinkedIn profiles, and websites.",
                                        "properties": {
                                            "emails": {"type": "array", "description": "list of emails", "items": {"type": "string"}},
                                            "phones": {"type": "array", "description": "list of phones", "items": {"type": "string"}},
                                            "addresses": {"type": "array", "description": "list of addresses", "items": {"type": "string"}},
                                            "linkedins": {"type": "array", "description": "list of linkedins", "items": {"type": "string"}},
                                            "websites": {"type": "array", "description": "list of websites", "items": {"type": "string"}}
                                        }
                                    },
                                    "objective": {
                                        "type": "string",
                                        "description": "The career objective of the candidate."
                                    },
                                    "skills": {
                                        "type": "array",
                                        "description": "The list of skills possessed by the candidate.",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "experience": {
                                        "type": "array",
                                        "description": "The list of working experience of the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "experience description with years",
                                        }
                                    },
                                    "education": {
                                        "type": "array",
                                        "description": "The educational qualifications with corresponding years of the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "detail of education with years",
                                        }
                                    },
                                    "certifications": {
                                        "type": "array",
                                        "description": "The certifications obtained by the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "certifications with date and description",
                                        }
                                    },
                                    "languages": {
                                        "type": "array",
                                        "description": "The languages known by the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "languages known by the candidate, if not provided infer it from the candidate text.",
                                        }
                                    },
                                    "references": {
                                        "type": "array",
                                        "description": "The references provided by the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "references of the candidate",
                                        }
                                    },
                                    "description": {
                                        "type": "string",
                                        "description": "A general description of the candidate."
                                    },
                                    "nationality": {
                                        "type": "string",
                                        "description": "The nationality of the candidate."
                                    },
                                    "date_of_birth": {
                                        "type": "string",
                                        "description": "The date of birth of the candidate."
                                    },
                                    "hobbies": {
                                        "type": "array",
                                        "description": "The hobbies and interests of the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "hobbies description",
                                        }
                                        
                                    },
                                    "volunteer_work": {
                                        "type": "string",
                                        "description": "Information about the candidate's volunteer work."
                                    },
                                    "publications": {
                                        "type": "array",
                                        "description": "Publications authored by the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "Publications description",
                                        }
                                    },
                                    "awards": {
                                        "type": "array",
                                        "description": "Awards received by the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "award description",
                                        }
                                    },
                                    "affiliations": {
                                        "type": "array",
                                        "description": "Professional affiliations of the candidate.",
                                        "items": {
                                            "type": "string",
                                            "description": "experience with years",
                                        }
                                    }
                                },
                            },
                        },
                    },
                "required": ["candidates"],
                },
            }
        ]

    def _function_description_match_candidate(self):
        return [
            {
                "name": "match_candidate_with_job",
                "description": "returns a list of matching id candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidates": {
                            "type": "array",
                            "description": "List of candidates",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "string", "description": "Candidate ID"},
                                    "matches": {"type": "boolean", "description": "true if the candidates matches"},
                                    "matching_reason": {"type": "string", "description": "an elaboration of why the candidate matches or not for the job position. Mention highlights and key skills"}
                                },
                            },
                        },
                    },
                    "required": ["candidates"],
                },
            }
        ]

    def _class_cv_description_parse(self):
        summary_of_qualification_tips = """Total experience in years/months This duration should be equal to total duration of the projects in the Experience section Types of applications that you have worked on (web, mobile, integration, desktop, embedded, database, business intelligence) Main technologies Methodologies (Scrum, etc) Software development life cycle (SDLC) (working with requirements, architecture, design, coding, testing, debugging, building, deploying, publishing) Impressive architecture attributes on some projects if any (high loaded, scalable, secured, available, reliable, etc.).                 Interests in IT. 
                Personal qualities (good team player, good communication skills, love to learn new, etc)"""

        return [
            {
                "name": "parse_candidates",
                "description": "parse candidates from a text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidates": {
                            "type": "array",
                            "description": "List of candidates",
                            "items": {
                                "type": "object",
                                "properties": 
                                {
                                    "name": {"type": "string", "description": "The name of the CV owner."},
                                    "position": {"type": "string", "description": "The position of the CV owner."},
                                    "summary": {"type": "string", "description": "Summary of the CV owner."},
                                    "summary_of_qualifications": {"type": "string", "description": "Summary of qualifications."},
                                    "skills": {
                                        "type": "array",
                                        "description": "List of skill categories.",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "name": {"type": "string", "description": "Name of the skill category."},
                                                "skills": {
                                                    "type": "array",
                                                    "description": "List of skills within the category.",
                                                    "items": {"type": "string"}
                                                }
                                            }
                                        }
                                    },
                                    "experience": {
                                        "type": "array",
                                        "description": "List of work experience projects.",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "name": {"type": "string", "description": "Name of the project."},
                                                "description": {"type": "string", "description": "Description of the project."},
                                                "customer": {"type": "string", "description": "Customer of the project."},
                                                "duration": {"type": "string", "description": "Duration of the project."},
                                                "role": {"type": "string", "description": "Role in the project."},
                                                "responsibilities": {"type": "string", "description": "Responsibilities in the project."},
                                                "team_size": {"type": "string", "description": "Team size in the project."},
                                                "tools_technologies": {"type": "string", "description": "Tools and technologies used in the project."}
                                            }
                                        }
                                    },
                                    "certifications": {
                                        "type": "array",
                                        "description": "List of certifications.",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "name": {"type": "string", "description": "Name of the certification."},
                                                "year": {"type": "string", "description": "Year of the certification."},
                                                "logo": {"type": "string", "description": "Logo of the certification."},
                                                "link": {"type": "string", "description": "Link to the certification."}
                                            }
                                        }},
                                    "education": {
                                        "type": "array",
                                        "description": "List of educational qualifications.",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "degree": {"type": "string", "description": "Degree obtained with the corresponding year."},
                                                "school_name": {"type": "string", "description": "Name of the school."},
                                                "department": {"type": "string", "description": "Department of education."}
                                            }
                                        }
                                    }
                                },
                        },
                    },
                },
                "required": ["candidates"],
                },
            }
            
        ]
