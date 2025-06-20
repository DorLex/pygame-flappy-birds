import pygame
from pygame.time import Clock

from src.constants import GameConditionEnum
from src.models.bird import bird
from src.rendering.common_data import item_container
from src.rendering.painter import Painter
from src.rendering.spawner import Spawner
from src.settings import FPS

pygame.init()

clock: Clock = Clock()

spawner: Spawner = Spawner(item_container)
painter: Painter = Painter(item_container)


def main() -> None:
    while True:
        clock.tick(FPS)

        # Управление:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    item_container.game_condition = GameConditionEnum.play
                    bird.fall_speed = -14

        # Рендеринг:
        spawner.background_spawn()
        spawner.background_movement()
        painter.draw_background()

        painter.draw_bird()

        if item_container.game_condition == GameConditionEnum.play:
            spawner.pipes_spawn()
            spawner.pipes_movement()
            painter.draw_pipes()

            spawner.bird_falling()
            spawner.check_collisions()
            spawner.increase_score()

        painter.draw_score()

        pygame.display.update()


if __name__ == '__main__':
    main()
