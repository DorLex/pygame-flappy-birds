import pygame
from pygame import Rect

from src.constants import Window

pygame.init()


class Bird:
    width: int = 34
    height: int = 24
    x: int = Window.width // 3
    y: int = Window.height // 2
    fall_speed: int = 0
    collision_model: Rect = Rect(x, y, width, height)


bird: Bird = Bird()
