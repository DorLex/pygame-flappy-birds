import pygame
from pygame import Surface, display
from pygame.font import Font, SysFont

from src.constants import Window

pygame.init()

screen: Surface = display.set_mode((Window.width, Window.height))
font: Font = SysFont('Comic Sans MS', 46, bold=True)
