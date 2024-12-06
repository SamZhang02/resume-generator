from abc import abstractmethod, ABC
from App.models.resume import Resume


class Renderer(ABC):

    @abstractmethod
    def __init__(self, out_path: str) -> None:
        self.out_path = out_path

    @abstractmethod
    def render_document(self, resume: Resume): ...
