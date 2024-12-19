from dataclasses import dataclass
from ..tools.validation import validate_types


@dataclass
@validate_types
class EducationItem:
    institution: str
    degree: str
    location: str | None = None
    date: str | None = None
    link: str | None = None
