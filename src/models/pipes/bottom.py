import pygame
from pygame import Rect

from src import settings
from src.models.pipes.abstract import AbstractPipe

pygame.init()


class BottomPipe(AbstractPipe):
    def __init__(self, random_height: int) -> None:
        super().__init__(random_height)
        self.y = settings.WINDOW_HEIGHT - self.random_height
        self.collision_model: Rect = self.get_rectangle()
