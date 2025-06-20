import pygame
from pygame.time import Clock

from src.constants import GameConditionEnum
from src.models.bird import bird
from src.rendering.common_data import entity_container
from src.rendering.entity_manager import EntityManager
from src.rendering.painter import Painter
from src.settings import FPS

pygame.init()

clock: Clock = Clock()

entity_manager: EntityManager = EntityManager(entity_container)
painter: Painter = Painter(entity_container)


def main() -> None:
    while True:
        clock.tick(FPS)

        # Управление:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    entity_container.game_condition = GameConditionEnum.play
                    bird.fall_speed = -14

        # Рендеринг:
        entity_manager.background_spawn()
        entity_manager.background_movement()
        painter.draw_background()

        painter.draw_bird()

        if entity_container.game_condition == GameConditionEnum.play:
            entity_manager.pipes_spawn()
            entity_manager.pipes_movement()
            painter.draw_pipes()

            entity_manager.bird_falling()
            entity_manager.check_collisions()
            entity_manager.increase_score()

        painter.draw_score()

        pygame.display.update()


if __name__ == '__main__':
    main()
