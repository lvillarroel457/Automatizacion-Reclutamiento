from uuid import uuid4

from main.domain.contact_information import ContactInformation

class Candidate:
    def __init__(self, candidate_id=None, full_name=None, contact_information: ContactInformation=None, objective=None, skills=None, experience=None, education=None, certifications=None, languages=None, references=None, description=None, nationality=None, date_of_birth=None, hobbies=None, volunteer_work=None, publications=None, awards=None, affiliations=None):
        if candidate_id is None:
            self.candidate_id = str(uuid4())
        else:
            self.candidate_id = candidate_id

        self.full_name = full_name
        self.contact_information = contact_information
        self.objective = objective
        self.skills = skills if skills else []
        self.experience = experience if experience else []
        self.education = education if education else []
        self.certifications = certifications if certifications else []
        self.languages = languages if languages else []
        self.references = references if references else []
        self.description = description
        self.nationality = nationality
        self.date_of_birth = date_of_birth
        self.hobbies = hobbies if hobbies else []
        self.volunteer_work = volunteer_work
        self.publications = publications
        self.awards = awards
        self.affiliations = affiliations if affiliations else []

    @classmethod
    def from_json(cls, json_data):
        contact_info = ContactInformation.from_json(json_data['contact_information']) if 'contact_information' in json_data else None

        return cls(
            candidate_id=json_data.get('candidate_id'),
            full_name=json_data.get('full_name'),
            contact_information=contact_info,
            objective=json_data.get('objective'),
            skills=json_data.get('skills'),
            experience=json_data.get('experience'),
            education=json_data.get('education'),
            certifications=json_data.get('certifications'),
            languages=json_data.get('languages'),
            references=json_data.get('references'),
            description=json_data.get('description'),
            nationality=json_data.get('nationality'),
            date_of_birth=json_data.get('date_of_birth'),
            hobbies=json_data.get('hobbies'),
            volunteer_work=json_data.get('volunteer_work'),
            publications=json_data.get('publications'),
            awards=json_data.get('awards'),
            affiliations=json_data.get('affiliations')
        )

    def to_json(self):
        return {
            "candidate_id": self.candidate_id,
            "full_name": self.full_name,
            "contact_information": self.contact_information.to_json() if self.contact_information else None,
            "objective": self.objective,
            "skills": self.skills,
            "experience": self.experience,
            "education": self.education,
            "certifications": self.certifications,
            "languages": self.languages,
            "references": self.references,
            "description": self.description,
            "nationality": self.nationality,
            "date_of_birth": self.date_of_birth,
            "hobbies": self.hobbies,
            "volunteer_work": self.volunteer_work,
            "publications": self.publications,
            "awards": self.awards,
            "affiliations": self.affiliations
        }

    def __str__(self):
        return (
            f"ID: {self.candidate_id}\n"
            f"Name: {self.full_name}\n"
            f"Contact Information:\n{str(self.contact_information) if self.contact_information else 'N/A'}\n"
            f"Objective: {self.objective}\n"
            f"Skills: {', '.join(self.skills) if self.skills else 'N/A'}\n"
            f"Experience: {self.experience}\n"
            f"Education: {self.education}\n"
            f"Certifications: {self.certifications}\n"
            f"Languages: {', '.join(self.languages) if self.languages else 'N/A'}\n"
            f"References: {self.references}\n"
            f"Description: {self.description}\n"
            f"Nationality: {self.nationality}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"Hobbies: {', '.join(self.hobbies) if self.hobbies else 'N/A'}\n"
            f"Volunteer Work: {self.volunteer_work}\n"
            f"Publications: {self.publications}\n"
            f"Awards: {self.awards}\n"
            f"Affiliations: {', '.join(self.affiliations) if self.affiliations else 'N/A'}"
        )
