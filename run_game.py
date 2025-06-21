import pygame
from pygame.time import Clock

from src.constants import GameConditionEnum
from src.control import control
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
        control()

        # Рендеринг:
        entity_manager.spawn_background()
        entity_manager.move_background()
        painter.draw_background()

        painter.draw_bird()

        if entity_container.game_condition == GameConditionEnum.play:
            entity_manager.spawn_pipes()
            entity_manager.move_pipes()
            painter.draw_pipes()

            entity_manager.bird_gravity()
            entity_manager.check_collisions()
            entity_manager.increase_score()

        painter.draw_score()

        pygame.display.update()


if __name__ == '__main__':
    main()
