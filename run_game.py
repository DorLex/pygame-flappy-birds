import pygame

from project.settings import FPS
from project.rendering import Game, Spawner, Painter
from project.models import bird

pygame.init()

clock = pygame.time.Clock()

game = Game()
spawner = Spawner(game)
painter = Painter(game, spawner)


def main():
    while True:

        # Управление
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.game_condition = 'play'
                    bird.fall_speed = -14

        # Обработка
        spawner.game_stage()
        spawner.background_spawn()
        spawner.background_movement()
        spawner.pipes_spawn()
        spawner.pipes_movement()
        spawner.collisions()
        spawner.update_score()

        # Отрисовка
        painter.draw_background()
        painter.draw_bird()
        painter.draw_pipes()
        painter.draw_score()

        pygame.display.update()

        clock.tick(FPS)


if __name__ == '__main__':
    main()
