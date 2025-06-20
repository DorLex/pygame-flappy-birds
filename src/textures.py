import pygame
from pygame import Surface, image

from src.constants import textures_folder

pygame.init()

background_img_block: Surface = image.load(textures_folder / 'background.png').convert_alpha()
bird_frames: Surface = image.load(textures_folder / 'bird.png').convert_alpha()
pipe_top: Surface = image.load(textures_folder / 'pipe_top.png').convert_alpha()
pipe_bottom: Surface = image.load(textures_folder / 'pipe_bottom.png').convert_alpha()
