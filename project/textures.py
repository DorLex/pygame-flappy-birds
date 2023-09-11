import pygame

from . import settings

pygame.init()

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

font = pygame.font.SysFont('Comic Sans MS', 46, bold=True)

background_img_block = pygame.image.load('project/images/background.png').convert_alpha()
bird_frames = pygame.image.load('project/images/bird.png').convert_alpha()
pipe_top = pygame.image.load('project/images/pipe_top.png').convert_alpha()
pipe_bottom = pygame.image.load('project/images/pipe_bottom.png').convert_alpha()
