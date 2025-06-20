from random import randint

import pygame
from pygame import Rect

from src import settings, textures
from src.models.bird import bird
from src.models.pipes.abstract import AbstractPipe
from src.models.pipes.bottom import BottomPipe
from src.models.pipes.top import TopPipe
from src.models.score import Score


class DataContainer:
    def __init__(self) -> None:
        self.bird_frame_num = 0
        self.background_rectangles: list[Rect] = [Rect(0, 0, 288, 600)]
        self.pipes = []
        self.pipes_to_left_of_bird = []
        self.game_condition = 'start'
        self.score = 0


class Spawner:
    def __init__(self, container: DataContainer) -> None:
        self.container = container

    def _game_over(self) -> None:
        self.container.game_condition = 'start'
        self.container.score = 0
        self.container.pipes = []
        bird.collision_model.y = settings.WINDOW_HEIGHT // 2

    def check_collisions(self) -> None:
        if bird.collision_model.bottom >= settings.WINDOW_HEIGHT or bird.collision_model.top <= 0:
            self._game_over()
            return

        for pipe in self.container.pipes:
            if bird.collision_model.colliderect(pipe.collision_model):
                self._game_over()

    def update_score(self) -> None:
        for pipe in self.container.pipes:
            if (
                pipe.collision_model.right <= bird.collision_model.left
                and pipe not in self.container.pipes_to_left_of_bird
            ):
                self.container.pipes_to_left_of_bird.append(pipe)
                self.container.score += 0.5

    def pipes_spawn(self) -> None:
        distance_for_next_pipe: int = settings.WINDOW_WIDTH - settings.DISTANCE_BETWEEN_PIPES

        if not self.container.pipes or self.container.pipes[-1].collision_model.x < distance_for_next_pipe:
            random_height: int = randint(100, 300)
            self.container.pipes.append(TopPipe(random_height))
            self.container.pipes.append(BottomPipe(random_height))

    def _pipe_remove(self, pipe: AbstractPipe) -> None:
        self.container.pipes.remove(pipe)
        if pipe in self.container.pipes_to_left_of_bird:
            self.container.pipes_to_left_of_bird.remove(pipe)

    def pipes_movement(self) -> None:
        for pipe in reversed(self.container.pipes):
            pipe.collision_model.x -= 5

            if pipe.collision_model.right < 0:
                self._pipe_remove(pipe)

    def background_spawn(self) -> None:
        if self.container.background_rectangles[-1].right <= settings.WINDOW_WIDTH:
            self.container.background_rectangles.append(
                pygame.Rect(self.container.background_rectangles[-1].right, 0, 288, settings.WINDOW_HEIGHT),
            )

    def _background_remove(self, bg_rect: Rect) -> None:
        self.container.background_rectangles.remove(bg_rect)

    def background_movement(self) -> None:
        for bg_rect in reversed(self.container.background_rectangles):
            bg_rect.x -= 1

            if bg_rect.right < 0:
                self._background_remove(bg_rect)

    def bird_falling(self) -> None:
        bird.fall_speed += 1
        bird.collision_model.y += bird.fall_speed


class Painter:
    def __init__(self, container: DataContainer) -> None:
        self.container = container

    def draw_background(self) -> None:
        for bg_rect in self.container.background_rectangles:
            textures.screen.blit(textures.background_img_block, bg_rect)

    def draw_bird(self) -> None:
        self.container.bird_frame_num = (self.container.bird_frame_num + 0.2) % 4
        img_bird = textures.bird_frames.subsurface(
            settings.BIRD_WIDTH * int(self.container.bird_frame_num),
            0,
            settings.BIRD_WIDTH,
            settings.BIRD_HEIGHT,
        )

        if self.container.game_condition == 'play':
            img_bird = pygame.transform.rotate(img_bird, -bird.fall_speed * 3)

        textures.screen.blit(img_bird, bird.collision_model)

    def draw_pipes(self) -> None:
        for pipe in self.container.pipes:
            if type(pipe) == TopPipe:
                rect = textures.pipe_top.get_rect(bottomleft=pipe.collision_model.bottomleft)
                textures.screen.blit(textures.pipe_top, rect)
            else:
                rect = textures.pipe_bottom.get_rect(topleft=pipe.collision_model.topleft)
                textures.screen.blit(textures.pipe_bottom, rect)

    def draw_score(self) -> None:
        score: Score = Score(self.container.score)
        textures.screen.blit(score.text, (settings.WINDOW_WIDTH // 2, 30))
