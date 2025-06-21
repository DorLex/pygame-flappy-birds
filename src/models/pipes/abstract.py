import pygame
from pygame import Rect

from src.constants import Window

pygame.init()


class BasePipe(Rect):
    def __init__(self, random_height: int) -> None:
        x: int = Window.width
        y: int = 0
        width: int = 52  # == размеру текстуры
        height: int = 400  # == размеру текстуры

        super().__init__(x, y, width, height)

        self.random_height: int = random_height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BasePipe):
            return False
        return id(other) == id(self)  # для корректного удаления из EntityContainer.pipes и EntityContainer.passed_pipes

    def __hash__(self) -> int:
        return hash(id(self))  # для корректного удаления из EntityContainer.pipes и EntityContainer.passed_pipes
