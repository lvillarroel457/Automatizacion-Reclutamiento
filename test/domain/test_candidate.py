import unittest
from main.domain.contact_information import ContactInformation
from main.domain.candidate import Candidate

class TestCandidate(unittest.TestCase):
    def test_init_with_no_candidate_id(self):
        candidate = Candidate(full_name="John Doe")
        self.assertIsNotNone(candidate.candidate_id)
        self.assertIsInstance(candidate.candidate_id, str)

    def test_init_with_candidate_id(self):
        candidate_id = "123456789"
        candidate = Candidate(candidate_id=candidate_id, full_name="John Doe")
        self.assertEqual(candidate.candidate_id, candidate_id)

    def test_to_json(self):
        contact_info = ContactInformation(emails=["john.doe@example.com"], phones=["123-456-7890"])
        candidate = Candidate(
            candidate_id="123456789",
            full_name="John Doe",
            contact_information=contact_info,
            objective="Seeking a challenging position in Software Engineering",
            skills=["Python", "Java", "C++"],
            experience=["Software Developer at TechCorp Solutions"],
            education=["Bachelor of Science in Computer Science"],
            languages=["English", "Spanish"],
            references=["John Smith", "Jane Doe"],
            description="Motivated and skilled software engineer",
            nationality="American",
            date_of_birth="1990-01-01",
            hobbies=["Reading", "Traveling"],
            volunteer_work="Local technology workshop",
            publications=None,
            awards="Employee of the Month",
            affiliations=["IEEE", "ACM"]
        )
        expected_json = {
            "candidate_id": "123456789",
            "full_name": "John Doe",
            "contact_information": {
                "emails": ["john.doe@example.com"],
                "phones": ["123-456-7890"],
                "addresses": [],
                "linkedins": [],
                "websites": []
            },
            "objective": "Seeking a challenging position in Software Engineering",
            "skills": ["Python", "Java", "C++"],
            "experience": ["Software Developer at TechCorp Solutions"],
            "education": ["Bachelor of Science in Computer Science"],
            "languages": ["English", "Spanish"],
            "references": ["John Smith", "Jane Doe"],
            "description": "Motivated and skilled software engineer",
            "nationality": "American",
            "date_of_birth": "1990-01-01",
            "hobbies": ["Reading", "Traveling"],
            "volunteer_work": "Local technology workshop",
            "publications": None,
            "awards": "Employee of the Month",
            "affiliations": ["IEEE", "ACM"]
        }
        # self.assertEqual(candidate.to_json(), expected_json)

    def test_from_json(self):
        json_data = {
            "candidate_id": "123456789",
            "full_name": "John Doe",
            "contact_information": {
                "emails": ["john.doe@example.com"],
                "phones": ["123-456-7890"],
                "addresses": [],
                "linkedins": [],
                "websites": []
            },
            "objective": "Seeking a challenging position in Software Engineering",
            "skills": ["Python", "Java", "C++"],
            "experience": ["Software Developer at TechCorp Solutions"],
            "education": ["Bachelor of Science in Computer Science"],
            "languages": ["English", "Spanish"],
            "references": ["John Smith", "Jane Doe"],
            "description": "Motivated and skilled software engineer",
            "nationality": "American",
            "date_of_birth": "1990-01-01",
            "hobbies": ["Reading", "Traveling"],
            "volunteer_work": "Local technology workshop",
            "publications": None,
            "awards": "Employee of the Month",
            "affiliations": ["IEEE", "ACM"]
        }
        candidate = Candidate.from_json(json_data)
        self.assertEqual(candidate.candidate_id, "123456789")
        self.assertEqual(candidate.full_name, "John Doe")
        self.assertIsInstance(candidate.contact_information, ContactInformation)
        self.assertEqual(candidate.contact_information.emails, ["john.doe@example.com"])
        self.assertEqual(candidate.contact_information.phones, ["123-456-7890"])
        self.assertEqual(candidate.objective, "Seeking a challenging position in Software Engineering")
        self.assertEqual(candidate.skills, ["Python", "Java", "C++"])
        self.assertEqual(candidate.experience, ["Software Developer at TechCorp Solutions"])
        self.assertEqual(candidate.education, ["Bachelor of Science in Computer Science"])
        self.assertEqual(candidate.languages, ["English", "Spanish"])
        self.assertEqual(candidate.references, ["John Smith", "Jane Doe"])
        self.assertEqual(candidate.description, "Motivated and skilled software engineer")
        self.assertEqual(candidate.nationality, "American")
        self.assertEqual(candidate.date_of_birth, "1990-01-01")
        self.assertEqual(candidate.hobbies, ["Reading", "Traveling"])
        self.assertEqual(candidate.volunteer_work, "Local technology workshop")
        self.assertIsNone(candidate.publications)
        self.assertEqual(candidate.awards, "Employee of the Month")
        self.assertEqual(candidate.affiliations, ["IEEE", "ACM"])

if __name__ == '__main__':
    unittest.main()
