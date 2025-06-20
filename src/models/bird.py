import pygame
from pygame import Rect

from src.constants import Window

pygame.init()


class Bird:
    width: int = 34
    height: int = 24
    x: int = Window.width // 3
    base_y: int = Window.height // 2
    y: int = base_y
    fall_speed: int = 0
    jump_speed: int = 14
    collision_model: Rect = Rect(x, y, width, height)


bird: Bird = Bird()
