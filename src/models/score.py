import pygame

from src import textures

pygame.init()


class Score:
    def __init__(self, score: int | float) -> None:
        self.text = textures.font.render(f'{int(score)}', True, 'white')
