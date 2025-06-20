import pygame

from src.components import font

pygame.init()


class Score:
    def __init__(self, score: int | float) -> None:
        self.text = font.render(f'{int(score)}', True, 'white')
