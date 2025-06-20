import pygame
from pygame import Rect

from src.models.pipes.abstract import AbstractPipe

pygame.init()


class TopPipe(AbstractPipe):
    def __init__(self, random_height: int) -> None:
        super().__init__(random_height)
        self.y -= self.random_height
        self.collision_model: Rect = self._create_collision_model()
