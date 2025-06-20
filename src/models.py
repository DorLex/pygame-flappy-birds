from abc import ABC, abstractmethod

import pygame
from pygame import Rect

from src import settings, textures

pygame.init()


class Bird:
    def __init__(self) -> None:
        self.x = settings.WINDOW_WIDTH // 3
        self.y = settings.WINDOW_HEIGHT // 2
        self.fall_speed = 0
        self.model = pygame.Rect(self.x, self.y, settings.BIRD_WIDTH, settings.BIRD_HEIGHT)


class Pipe(ABC):
    @abstractmethod
    def __init__(self, random_height: int) -> None:
        self.x = settings.WINDOW_WIDTH
        self.y = 0
        self.width = settings.PIPE_WIDTH
        self.height = settings.PIPE_HEIGHT
        self.random_height = random_height

    def get_rectangle(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)


class TopPipe(Pipe):
    def __init__(self, random_height: int) -> None:
        super().__init__(random_height)
        self.height -= self.random_height
        self.model: Rect = self.get_rectangle()


class BottomPipe(Pipe):
    def __init__(self, random_height: int) -> None:
        super().__init__(random_height)
        self.y = settings.WINDOW_HEIGHT - self.random_height

        self.model: Rect = self.get_rectangle()


class Score:
    def __init__(self, score: int | float) -> None:
        self.text = textures.font.render(f'{int(score)}', True, 'white')


bird: Bird = Bird()
