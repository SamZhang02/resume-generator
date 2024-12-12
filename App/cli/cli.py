from InquirerPy import inquirer

from ..models.resume import Resume, ResumeBuilder


class CLI:
    def __init__(self, full_resume: Resume) -> None:
        self.full_resume = full_resume
        self.custom_resume_builder = ResumeBuilder(full_resume.name)
        self.custom_resume = None

    def _query_contacts(self):
        contacts = self.full_resume.contacts

        to_include = inquirer.checkbox(
            message="Select contact methods to include:",
            choices=[contact.text for contact in contacts],
            vi_mode=True,
            enabled_symbol="[x]",
            disabled_symbol="[ ]",
        ).execute()

        return [contact for contact in contacts if contact.text in to_include]

    def _query_education(self):
        educations = self.full_resume.educations

        to_include = inquirer.checkbox(
            message="Select education experiences to include:",
            choices=[
                f"{education.institution} - {education.degree}"
                for education in educations
            ],
            vi_mode=True,
            enabled_symbol="[x]",
            disabled_symbol="[ ]",
        ).execute()

        return [
            education
            for education in educations
            if f"{education.institution} - {education.degree}" in to_include
        ]

    def _query_experiences(self):
        experiences = self.full_resume.experiences

        to_include = inquirer.checkbox(
            message="Select experiences to include:",
            choices=[
                f"{experience.company} - {experience.title} - {experience.date}"
                for experience in experiences
            ],
            vi_mode=True,
            enabled_symbol="[x]",
            disabled_symbol="[ ]",
        ).execute()

        return [
            experience
            for experience in experiences
            if f"{experience.company} - {experience.title} - {experience.date}"
            in to_include
        ]

    def _query_projects(self):
        projects = self.full_resume.projects

        to_include = inquirer.checkbox(
            message="Select projects to include:",
            choices=[project.name for project in projects],
            vi_mode=True,
            enabled_symbol="[x]",
            disabled_symbol="[ ]",
        ).execute()

        return [project for project in projects if project.name in to_include]

    def _query_skills(self):
        skills = self.full_resume.skills

        to_include = inquirer.checkbox(
            message="Select skill sections to include:",
            choices=[f"{skill.category}: {skill.items}" for skill in skills],
            vi_mode=True,
            enabled_symbol="[x]",
            disabled_symbol="[ ]",
        ).execute()

        return [
            skill
            for skill in skills
            if f"{skill.category}: {skill.items}" in to_include
        ]

    def start(self):
        methods = [
            (self.custom_resume_builder.add_contact, self._query_contacts),
            (self.custom_resume_builder.add_education, self._query_education),
            (self.custom_resume_builder.add_experience, self._query_experiences),
            (self.custom_resume_builder.add_project, self._query_projects),
            (self.custom_resume_builder.add_skill, self._query_skills),
        ]

        for add_item, query in methods:
            for item in query():
                if not item:
                    continue
                add_item(item)

        self.custom_resume = self.custom_resume_builder.build()
