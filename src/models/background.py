from pygame import Rect

from src.constants import Window


class Background:
    def __init__(self, x: int = 0) -> None:
        self.x: int = x
        self.y: int = 0
        self.width: int = 288  # == размеру текстуры
        self.height: int = Window.height  # == размеру текстуры
        self.collision_model: Rect = self._create_collision_model()

    def _create_collision_model(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)
