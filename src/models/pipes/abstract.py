from abc import ABC, abstractmethod

import pygame
from pygame import Rect

from src.constants import Window

pygame.init()


class AbstractPipe(ABC):
    @abstractmethod
    def __init__(self, random_height: int) -> None:
        self.x: int = Window.width
        self.y: int = 0
        self.width: int = 52  # == размеру текстуры
        self.height: int = 400  # == размеру текстуры
        self.random_height: int = random_height
        self.collision_model: Rect | None = None

    def _create_collision_model(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)
