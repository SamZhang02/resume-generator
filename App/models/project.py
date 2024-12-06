from dataclasses import dataclass
from ..tools.validation import validate_types


@dataclass
@validate_types
class ProjectItem:
    name: str
    technologies: list[str]
    bulletpoints: list[str]
