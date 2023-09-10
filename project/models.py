from random import randint

import pygame

from . import settings
from . import textures

pygame.init()


class Bird:
    def __init__(self):
        self.x = settings.WINDOW_WIDTH // 3
        self.y = settings.WINDOW_HEIGHT // 2
        self.fall_speed = 0
        self.model = pygame.Rect(self.x, self.y, settings.BIRD_WIDTH, settings.BIRD_HEIGHT)


class Pipe:
    def __init__(self, random_height):
        self.x = settings.WINDOW_WIDTH
        self.y = 0
        self.width = settings.PIPE_WIDTH
        self.height = settings.PIPE_HEIGHT

        self.random_height = random_height

    def get_rectangle(self):
        rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        return rectangle


class TopPipe(Pipe):
    def __init__(self, random_height):
        super().__init__(random_height)
        self.height -= self.random_height

        self.model: pygame.Rect = self.get_rectangle()


class BottomPipe(Pipe):
    def __init__(self, random_height):
        super().__init__(random_height)
        self.y = settings.WINDOW_HEIGHT - self.random_height

        self.model: pygame.Rect = self.get_rectangle()


class Score:
    def __init__(self, score):
        self.text = textures.font.render(str(int(score)), True, 'white')


bird = Bird()
