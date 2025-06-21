import pygame

from src.constants import Window
from src.models.pipes.abstract import BasePipe

pygame.init()


class BottomPipe(BasePipe):
    def __init__(self, random_height: int) -> None:
        super().__init__(random_height)
        self.y: int = Window.height - self.random_height
