import pygame
from pygame import Surface
from pygame.font import Font

from src import settings
from src.constants import textures_folder

pygame.init()

screen: Surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

font: Font = pygame.font.SysFont('Comic Sans MS', 46, bold=True)

background_img_block: Surface = pygame.image.load(textures_folder / 'background.png').convert_alpha()
bird_frames: Surface = pygame.image.load(textures_folder / 'bird.png').convert_alpha()
pipe_top: Surface = pygame.image.load(textures_folder / 'pipe_top.png').convert_alpha()
pipe_bottom: Surface = pygame.image.load(textures_folder / 'pipe_bottom.png').convert_alpha()
