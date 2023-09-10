from random import randint

import pygame

from . import settings
from . import textures

pygame.init()


class Bird:
    def __init__(self):
        self.y = settings.WINDOW_HEIGHT // 2
        self.speed_y = 0
        self.model = pygame.Rect(settings.WINDOW_WIDTH // 3, self.y, 34, 24)


class Pipe:
    def __init__(self):
        self.pipe_differ = randint(100, 300)

    def create_pipe_top(self):
        pipe_top = pygame.Rect((settings.WINDOW_WIDTH, 0),
                               (settings.PIPE_WIDTH, settings.PIPE_LENGTH - self.pipe_differ))
        return pipe_top

    def create_pipe_bottom(self):
        pipe_bottom = pygame.Rect((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT - self.pipe_differ),
                                  (settings.PIPE_WIDTH, settings.PIPE_LENGTH))
        return pipe_bottom


class Score:
    def __init__(self, score):
        self.text = textures.font.render(str(int(score)), True, 'white')


bird = Bird()
