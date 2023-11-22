from main.ports.recruiter import Recruiter
import os
import openai
from dotenv import load_dotenv, find_dotenv




class OpenAiRecruiter(Recruiter):


    def __init__(self):
        _ = load_dotenv(find_dotenv())
        openai.api_key=os.getenv("OPENAI_API_KEY")
        self.model_selected = "gpt-4-0613"  

    def parse_candidate(self, candidates_contents):

        user_prompt = f"Please parse self text: {''.join(candidates_contents)} into a json of cv using the function. Remove all slashes (/,\). Don't return Unicode"
        completion = openai.ChatCompletion.create(
            model=self.model_selected,
            messages=[{"role": "system", "content": "You are an asisstant and you must use the function you are given. Don't return Unicode"},
            {"role": "user", "content": user_prompt}],
            functions=self._function_parse_cv(),
            function_call={"name": "parse_candidates"},
            temperature=0
        )

        output = completion.choices[0].message
        candidates = output.function_call.arguments

        return candidates


    def _function_parse_cv(self):
        return [
            {
                "name": "parse_candidates",
                "description": "Parse candidates from a text.  Remove all slashes (/,\)",
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
                                                "department": {"type": "string", "description": "Department of education."},
                                                "year": {"type": "string", "description": "Year of the certification."},
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
