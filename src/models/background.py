from pygame import Rect

from src.constants import Window


class Background(Rect):
    def __init__(self, x: int = 0) -> None:
        y: int = 0
        width: int = 288  # == размеру текстуры
        height: int = Window.height  # == размеру текстуры

        super().__init__(x, y, width, height)
