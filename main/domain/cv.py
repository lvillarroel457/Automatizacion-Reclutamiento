class SkillCategory:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    @classmethod
    def from_json(cls, json_data):
        name = json_data['name']
        skills = json_data['skills']
        return cls(name, skills)

    def to_json(self):
        return {
            'name': self.name,
            'skills': self.skills
        }

    def __str__(self):
        return f"SkillCategory(name={self.name}, skills={self.skills})"

class Project:
    def __init__(self, name, description, customer, duration, role, responsibilities, team_size, tools_technologies):
        self.name = name
        self.description = description
        self.customer = customer
        self.duration = duration
        self.role = role
        self.responsibilities = responsibilities
        self.team_size = team_size
        self.tools_technologies = tools_technologies

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'customer': self.customer,
            'duration': self.duration,
            'role': self.role,
            'responsibilities': self.responsibilities,
            'team_size': self.team_size,
            'tools_technologies': self.tools_technologies
        }

    def __str__(self):
        return f"Project(name={self.name}, description={self.description}, ...)"

class Certification:
    def __init__(self, name, year, logo=None, link=None):
        self.name = name
        self.year = year
        self.logo = logo
        self.link = link

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

    def to_json(self):
        return {
            'name': self.name,
            'year': self.year,
            'logo': self.logo,
            'link': self.link
        }

    def __str__(self):
        return f"Certification(name={self.name}, year={self.year}, link={self.link}, ...)"

class Education:
    def __init__(self, degree, school_name, department):
        self.degree = degree
        self.school_name = school_name
        self.department = department

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

    def to_json(self):
        return {
            'degree': self.degree,
            'school_name': self.school_name,
            'department': self.department
        }

    def __str__(self):
        return f"Education(degree={self.degree}, school_name={self.school_name}, ...)"

class CV:
    def __init__(self, name, position, summary, summary_of_qualifications, skills, experience, certifications, education):
        self.name = name
        self.position = position
        self.summary = summary
        self.summary_of_qualifications = summary_of_qualifications
        self.skills = skills
        self.experience = experience
        self.certifications = certifications
        self.education = education

    @classmethod
    def from_json(cls, json_data):
        skills = [SkillCategory.from_json(skill_data) for skill_data in json_data['skills']]
        experience = [Project.from_json(exp_data) for exp_data in json_data['experience']]
        certifications = [Certification.from_json(cert_data) for cert_data in json_data['certifications']]
        education = [Education.from_json(edu_data) for edu_data in json_data['education']]
        return cls(
            json_data['name'],
            json_data['position'],
            json_data['summary'],
            json_data['summary_of_qualifications'],
            skills,
            experience,
            certifications,
            education
        )

    def to_json(self):
        return {
            'name': self.name,
            'position': self.position,
            'summary': self.summary,
            'summary_of_qualifications': self.summary_of_qualifications,
            'skills': [skill.to_json() for skill in self.skills],
            'experience': [exp.to_json() for exp in self.experience],
            'certifications': [cert.to_json() for cert in self.certifications],
            'education': [edu.to_json() for edu in self.education]
        }

    def __str__(self):
        return f"CV(name={self.name}, position={self.position}, summary={self.summary}, ...)"
