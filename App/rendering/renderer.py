from abc import abstractmethod, ABC
from pathlib import Path
from ..models.resume import Resume


class Renderer(ABC):

    @abstractmethod
    def __init__(self, out_path: Path) -> None:
        self.out_path: Path = out_path

    @abstractmethod
    def render_document(self, resume: Resume): ...
