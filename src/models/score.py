import pygame
from pygame import Surface

from src.components import font
from src.constants import Window

pygame.init()


class Score:
    value: int | float = 0
    location: tuple = (Window.width // 2, 30)

    @property
    def texture(self) -> Surface:
        return font.render(f'{int(self.value)}', True, 'white')
