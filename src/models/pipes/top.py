import pygame

from src.models.pipes.abstract import BasePipe

pygame.init()


class TopPipe(BasePipe):
    def __init__(self, random_height: int) -> None:
        super().__init__(random_height)
        self.y -= self.random_height
