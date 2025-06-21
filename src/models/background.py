from pygame import Rect

from src.constants import Window


class Background(Rect):
    def __init__(self, x: int = 0) -> None:
        super().__init__(x, self.y, self.width, self.height)
        self.y: int = 0
        self.width: int = 288  # == размеру текстуры
        self.height: int = Window.height  # == размеру текстуры
