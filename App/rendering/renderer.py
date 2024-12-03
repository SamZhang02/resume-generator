from abc import abstractmethod


class Renderer():

    @abstractmethod
    def render_document(self):
        ...
