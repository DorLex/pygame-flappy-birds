import pygame
from pygame import Rect

from src.constants import Window

pygame.init()


class Bird(Rect):
    def __init__(self) -> None:
        x: int = Window.width // 3  # стартовое положение
        y: int = Window.height // 2  # стартовое положение
        width: int = 34  # == размеру одного кадра текстуры
        height: int = 24  # == размеру одного кадра текстуры

        super().__init__(x, y, width, height)

        self.base_y: int = y
        self.fall_speed: int = 0
        self.jump_speed: int = 14
        # self.frame_num: int = 0


bird: Bird = Bird()
