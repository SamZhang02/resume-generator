from typing import get_type_hints, get_origin, get_args, Union
import types


def validate_types(cls):
    """
    Cursed implementation of a decorator to validate types of all fields in a dataclass, including Optional and Union types.

    This is NOT a comprehensive type validation decorator, this only applies to specific types involved in the configuration json file
    """
    original_post_init = getattr(cls, "__post_init__", lambda self: None)

    def new_post_init(self):
        original_post_init(self)

        type_hints = get_type_hints(cls)

        for field_name, expected_type in type_hints.items():
            value = getattr(self, field_name)
            if not _is_valid_type(value, expected_type):
                raise TypeError(
                    f"Field '{field_name}' expected type '{expected_type}', "
                    f"but got value '{value}' of type '{type(value).__name__}'"
                )

    cls.__post_init__ = new_post_init
    return cls


def _is_valid_type(value, expected_type):
    """
    Validates if a value matches the expected type, including support for Optional and Union types.
    """
    origin = get_origin(expected_type)
    args = get_args(expected_type)

    if origin in [Union, types.UnionType]:
        return any(_is_valid_type(value, arg) for arg in args)

    if origin is list:
        return isinstance(value, list) and all(isinstance(item, args) for item in value)

    if value is None:
        return origin == None

    print(expected_type)
    return isinstance(value, expected_type)
