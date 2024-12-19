from pathlib import Path
from typing import Any
from ..models.contact import ContactItem
from ..models.education import EducationItem
from ..models.experience import ExperienceItem
from ..models.project import ProjectItem
from ..models.skill import SkillsItem
from ..models.resume import Resume, ResumeBuilder

import json


class Parser:
    keys:set[str] = set(["name", "education", "experience", "projects", "technical_skills"])

    def __init__(self, json_path:Path) -> None:
        self.json_path:Path = json_path

    def _validate_keys(self, info_dict):
        for key in self.keys:
            if key not in info_dict:
                raise ValueError(f"Info json is missing key {key}")

    def parse(self) -> Resume:
        info_dict = None
        with open(self.json_path) as fobj:
            info_dict = json.load(fobj)

        self._validate_keys(info_dict)

        name = info_dict["name"]
        resume_builder = ResumeBuilder(name)

        for contact in info_dict["contacts"]:
            resume_builder.add_contact(
                ContactItem(
                    contact["text"], contact["link"] if "link" in contact else ""
                )
            )

        for education in info_dict["education"]:
            resume_builder.add_education(
                EducationItem(
                    education["institution"],
                    education["degree"],
                    education["location"] if "location" in education else "",
                    date=education["date"] if "date" in education else "",
                    link=education["link"] if "link" in education else "" 
                )
            )

        for experience in info_dict["experience"]:
            resume_builder.add_experience(
                ExperienceItem(
                    experience["title"],
                    experience["company"],
                    experience["technologies"],
                    experience["bulletpoints"],
                    date=experience["date"] if "date" in experience else "",
                    location=experience["location"] if "location" in experience else "",
                    link=experience["link"] if "link" in experience else "" 
                )
            )

        for project in info_dict["projects"]:
            resume_builder.add_project(
                ProjectItem(
                    project["name"],
                    project["technologies"],
                    project["bulletpoints"],
                    date=project["date"] if "date" in project else "",
                    link=project["link"] if "link" in project else "" 
                )
            )

        for categorie, skills in info_dict["technical_skills"].items():
            resume_builder.add_skill(SkillsItem(categorie, skills))

        return resume_builder.build()


parser = Parser("./info.json")
resume = parser.parse()
