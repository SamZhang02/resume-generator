from dataclasses import dataclass
from ..tools.validation import validate_types

@dataclass
@validate_types
class SkillsItem:
    category:str
    items: list[str]
