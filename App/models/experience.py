from dataclasses import dataclass
from ..tools.validation import validate_types


@dataclass
@validate_types
class ExperienceItem:
    title: str
    company: str
    technologies: list[str]
    bulletpoints: list[str]
    date: str | None = None
    location: str | None = None
