from main.ports.recruiter import Recruiter
import os
import openai
from dotenv import load_dotenv, find_dotenv




class OpenAiRecruiter(Recruiter):

    MATCH_ERROR_MSG = "Error matching: "

    def __init__(self):
        super().__init__()
        _ = load_dotenv(find_dotenv())
        openai.api_key=os.getenv("OPENAI_API_KEY")
        self.model_selected = "gpt-3.5-turbo-0613"

    def parse_candidate(self, candidates_contents):
        try:
            user_prompt = f"Please parse self text: {''.join(candidates_contents)} into a json of cv. Do not add graduation year fields."
            completion = openai.ChatCompletion.create(
                model=self.model_selected,
                messages=[{"role": "user", "content": user_prompt}],
                functions=self._function_parse_cv(),
                function_call="auto",
            )

            output = completion.choices[0].message
            candidates = output.function_call.arguments

            return candidates
        except Exception as e:
            print(e.__dict__)

    def _function_parse_cv(self):
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
