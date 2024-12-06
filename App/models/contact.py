from dataclasses import dataclass
from ..tools.validation import validate_types

@dataclass
@validate_types
class ContactItem:
    text:str
    link: str | None
