import json
import os
from main.adapters.openai_job_matcher import OpenAiJobMatcher
import openai
import unittest

class TestOpenAiMatcher(unittest.TestCase):

    # def candidates_to_string(self, candidates):
    #     candidates_str_list = []
    #     for candidate in candidates:
    #         candidate_str = f"ID: {candidate['id']}, Description: {candidate['candidate_description']}, Email: {candidate['contact_data']['email']}, Phones: {', '.join(candidate['contact_data']['phones'])}, Sites: {', '.join(candidate['contact_data']['sites'])}"
    #         candidates_str_list.append(candidate_str)
    #     return ", ".join(candidates_str_list)

    # def match_candidate_with_job(self, candidates, job_position_text):
    #     openai.api_key = os.getenv("OPENAI_API_KEY")
    #     function_description_match_candidate = [
    #         {
    #             "name": "match_candidate_with_job",
    #             "description": "returns a list of matching id candidates.",
    #             "parameters": {
    #                 "type": "object",
    #                 "properties": {
    #                     "candidates": {
    #                         "type": "array",
    #                         "description": "List of candidates",
    #                         "items": {
    #                             "type": "object",
    #                             "properties": {
    #                                 "id": {"type": "string", "description": "Candidate ID"},
    #                                 "matches": {"type": "boolean", "description": "true if the candidates matches"},
    #                                 "matching_reason": {"type": "string", "description": "an elaboration of the matching index, why the candidate matches or not for the job position."}
    #                             },
    #                         },
    #                     },
    #                     "job_position_text": {
    #                         "type": "string",
    #                         "description": "The text description of the job position",
    #                     },
    #                 },
    #                 "required": ["candidates", "job_position_text"],
    #             },
    #         }
    #     ]

    #     user_prompt = f"Please match the following candidates with the job position: {job_position_text}. Candidates: {self.candidates_to_string(candidates)}, sort results from best match descending."
    #     completion = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo-0613",
    #         messages=[{"role": "user", "content": user_prompt}],
    #         functions=function_description_match_candidate,
    #         function_call="auto",
    #     )

    #     output = completion.choices[0].message
    #     match_results = json.loads(output.function_call.arguments)

    #     return match_results
    
    # def test_match_candidate_with_job(self):
    #     ##Arrange
    #     candidates = [
    #         {
    #             "id": "1",
    #             "contact_data": {"email": "candidate1@example.com", "phones": ["123456789"], "sites": ["example.com"]},
    #             "candidate_description": "Experienced software developer with expertise in Python and Java.",
    #         },
    #         {
    #             "id": "2",
    #             "contact_data": {"email": "candidate2@example.com", "phones": ["987654321"], "sites": ["example2.com"]},
    #             "candidate_description": "Junior developer with knowledge in Java.",
    #         }
    #     ]

    #     job_position_text = "Looking for a skilled developer with experience in Python."
    #     result = self.match_candidate_with_job(candidates, job_position_text)
    #     print("results: " + str(result))
    #     # Assuming the matching logic in the function, update the assertion as needed
    #     for candidate in result["candidates"]:
    #         self.assertIn("id", candidate)
    #         self.assertIn("matches", candidate)
    #         self.assertIn("matching_reason", candidate)
    
    def test_parse_candidate(self):
        #Arrange
        parser = OpenAiJobMatcher()
        poorly_formatted_cv = [
            '''
            John Smith 123 Main Street, Cityville, Country Email: 
            john.smith@email.com Phone: (123) 456-7890 Objective: Motivated and 
            skilled professional seeking a chalenging position in the feeld of Software
              Engineering to contribute technical expertise and drive innovative
                solutions in a dynamic and collaborative environment. Education: 
                Bachelor of Science in Computer Science University of Technology, 
                Cityville Graduated: May 2021 Skills: - Proficient in Java, Python,
                  C++, and JavaScript - Experienced in web development (HTML, CSS, React) 
                  - Knowledgeable in database management (SQL, MongoDB) - Familiarity 
                  with agile software development methodologies - Strong problem-solving 
                  and analytical skills - Excellent communication and teamwork abilities 
                  Work Experience: Software Developer Intern TechCorp Solutions, Cityville 
                  June 2020 - August 2020 - Collaborated with a team to develop and test 
                  new features for the company's flagship product. - Assisted in 
                  troubleshooting and resolving software defects to improve overall 
                  product quality. - Participated in code reviews and provided 
                  feedback for fellow developers. Technical Support Specialist 
                  TechHelp Services, Cityville October 2019 - May 2020 - Provided 
                  technical assistance to customers via phone, email, and chat, 
                  resolving software and hardware-related issues. - Escalated complex 
                  technical problems to the appropriate teams and ensured timely resolution. - 
                  Assisted in creating and updating support documentation for common issues. 
                  Projects: Online Bookstore Web Application - Developed a full-stack web
                    application using React, Node.js, and MongoDB to simulate an online bookstore. 
                    - Implemented user authentication, shopping cart functionality, and 
                    interactive book search features. - Deployed the application on 
                    Heroku and managed continuous integration with Git. AI Chatbot 
                    using Natural Language Processing - Created a chatbot using Python 
                    and the NLTK library to understand and respond to user queries. - 
                    Trained the chatbot with a dataset of sample conversations to improve
                      its accuracy and natural language understanding. Volunteer Experience: 
                      Community Technology Workshop - Volunteered at a local technology workshop, teaching basic coding 
                      concepts to underprivileged youth. Certifications: - Certified ScrumMaster (CSM) - Scrum Alliance -
                        AWS Certified Cloud Practitioner - Amazon Web Services Languages: - English (Native) - 
                        Spanish (Intermediate) References: Available upon request.
            ''']
        candidates = parser.parse(poorly_formatted_cv)
        print(candidates)
