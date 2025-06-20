from random import randint

from pygame import Rect

from src.constants import GameConditionEnum, Window
from src.models.bird import bird
from src.models.pipes.abstract import AbstractPipe
from src.models.pipes.bottom import BottomPipe
from src.models.pipes.top import TopPipe
from src.rendering.common_data import DataContainer
from src.settings import DISTANCE_BETWEEN_PIPES


class Spawner:
    def __init__(self, container: DataContainer) -> None:
        self.container = container

    def _game_over(self) -> None:
        self.container.game_condition = GameConditionEnum.start
        self.container.score = 0
        self.container.pipes = []
        bird.collision_model.y = Window.height // 2

    def check_collisions(self) -> None:
        if bird.collision_model.bottom >= Window.height or bird.collision_model.top <= 0:
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
        distance_for_next_pipe: int = Window.width - DISTANCE_BETWEEN_PIPES

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
        if self.container.backgrounds[-1].right <= Window.width:
            self.container.backgrounds.append(
                Rect(self.container.backgrounds[-1].right, 0, 288, Window.height),
            )

    def _background_remove(self, bg_rect: Rect) -> None:
        self.container.backgrounds.remove(bg_rect)

    def background_movement(self) -> None:
        for bg_rect in reversed(self.container.backgrounds):
            bg_rect.x -= 1

            if bg_rect.right < 0:
                self._background_remove(bg_rect)

    def bird_falling(self) -> None:
        bird.fall_speed += 1
        bird.collision_model.y += bird.fall_speed
