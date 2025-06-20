import pygame
from pygame import Rect

from src import settings

pygame.init()


class Bird:
    def __init__(self) -> None:
        self.x: int = settings.WINDOW_WIDTH // 3
        self.y: int = settings.WINDOW_HEIGHT // 2
        self.fall_speed: int = 0
        self.collision_model: Rect = Rect(self.x, self.y, settings.BIRD_WIDTH, settings.BIRD_HEIGHT)


bird: Bird = Bird()
