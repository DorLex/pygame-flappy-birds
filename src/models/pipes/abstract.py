from abc import ABC, abstractmethod

import pygame
from pygame import Rect

from src.constants import Window

pygame.init()


class AbstractPipe(ABC):
    @abstractmethod
    def __init__(self, random_height: int) -> None:
        self.x = Window.width
        self.y = 0
        self.width = 52
        self.height = 400
        self.random_height = random_height
        self.collision_model: Rect = self.get_rectangle()

    def get_rectangle(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)
