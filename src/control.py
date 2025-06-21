import pygame

from src.constants import GameConditionEnum
from src.models.bird import bird
from src.rendering.common_data import entity_container


def control() -> None:
    """Управление"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                entity_container.game_condition = GameConditionEnum.play
                bird.fall_speed = -bird.jump_speed
