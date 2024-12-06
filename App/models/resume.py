from dataclasses import dataclass
from ..models.contact import ContactItem
from ..models.education import EducationItem
from ..models.experience import ExperienceItem
from ..models.project import ProjectItem
from ..models.skill import SkillsItem

@dataclass
class Resume:
    name:str
    contacts: list[ContactItem] = list()
    educations: list[EducationItem] = list()
    experiences: list[ExperienceItem] = list()
    projects: list[ProjectItem] = list()
    skills: list[SkillsItem] = list()

class ResumeBuilder:
    def __init__(self, name: str):
        self._resume = Resume(name)

    def add_contact(self, contact_item: ContactItem):
        self._resume.contacts.append(contact_item)
        return self

    def add_education(self, education_item: EducationItem):
        self._resume.educations.append(education_item)
        return self

    def add_experience(self, experience_item: ExperienceItem):
        self._resume.experiences.append(experience_item)
        return self

    def add_project(self, project_item: ProjectItem):
        self._resume.projects.append(project_item)
        return self

    def add_skill(self, skill_item: SkillsItem):
        self._resume.skills.append(skill_item)
        return self

    def build(self):
        if not self._resume.contacts:
            raise ValueError("At least one contact item is required")
        if not self._resume.educations:
            raise ValueError("At least one education item is required")
        return self._resume
    

