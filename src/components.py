import pygame
from pygame import Surface, display
from pygame.font import Font, SysFont

from src import settings

pygame.init()

screen: Surface = display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
font: Font = SysFont('Comic Sans MS', 46, bold=True)
