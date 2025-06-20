import pygame
from pygame import Surface

from src.components import font

pygame.init()


class Score:
    def __init__(self, score: int | float) -> None:
        self.texture: Surface = font.render(f'{int(score)}', True, 'white')
