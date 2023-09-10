import pygame

from project.settings import FPS
from project.rendering import Renderer
from project.models import bird

pygame.init()

clock = pygame.time.Clock()

renderer = Renderer()


def main():
    while True:

        # Управление
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    renderer.game_condition = 'play'
                    bird.fall_speed = -14

        # Обработка
        renderer.game_stage()
        renderer.background_spawn()
        renderer.background_movement()
        renderer.pipes_spawn()
        renderer.pipes_movement()
        renderer.collisions()
        renderer.update_score()

        # Отрисовка
        renderer.draw_background()
        renderer.draw_bird()
        renderer.draw_pipes()
        renderer.draw_score()

        pygame.display.update()

        clock.tick(FPS)


if __name__ == '__main__':
    main()
