import pygame

from project.settings import FPS
from project.rendering import DataContainer, Spawner, Painter
from project.models import bird

pygame.init()

clock = pygame.time.Clock()

container = DataContainer()
spawner = Spawner(container)
painter = Painter(container)


def main():
    while True:
        clock.tick(FPS)

        # Управление
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    container.game_condition = 'play'
                    bird.fall_speed = -14

        spawner.background_spawn()
        spawner.background_movement()
        painter.draw_background()

        painter.draw_bird()

        if container.game_condition == 'play':
            spawner.pipes_spawn()
            spawner.pipes_movement()
            painter.draw_pipes()

            spawner.bird_falling()
            spawner.check_collisions()
            spawner.update_score()

        painter.draw_score()
        pygame.display.update()


if __name__ == '__main__':
    main()
