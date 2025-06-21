import pygame
from pygame import Rect

from src.constants import Window

pygame.init()


class Bird(Rect):
    def __init__(self) -> None:
        super().__init__(self.x, self.y, self.width, self.height)

        self.base_y: int = Window.height // 2  # стартовое положение

        self.x: int = Window.width // 3
        self.y: int = self.base_y
        self.width: int = 34  # == размеру одного кадра текстуры
        self.height: int = 24  # == размеру одного кадра текстуры

        self.fall_speed: int = 0
        self.jump_speed: int = 14


bird: Bird = Bird()
