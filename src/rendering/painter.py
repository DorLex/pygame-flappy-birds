import pygame
from pygame import Surface

from src import textures
from src.components import screen
from src.constants import GameConditionEnum, Window
from src.models.bird import bird
from src.models.pipes.top import TopPipe
from src.models.score import Score
from src.rendering.common_data import ItemContainer


class Painter:
    def __init__(self, container: ItemContainer) -> None:
        self.container = container

    def draw_background(self) -> None:
        for background in self.container.backgrounds:
            screen.blit(textures.background, background)

    def draw_bird(self) -> None:
        self.container.bird_frame_num = int((self.container.bird_frame_num + 0.2) % 4)
        bird_texture: Surface = textures.bird_frames.subsurface(
            bird.width * self.container.bird_frame_num,
            0,
            bird.width,
            bird.height,
        )

        if self.container.game_condition == GameConditionEnum.play:
            bird_texture: Surface = pygame.transform.rotate(bird_texture, -bird.fall_speed * 3)

        screen.blit(bird_texture, bird.collision_model)

    def draw_pipes(self) -> None:
        for pipe in self.container.pipes:
            if type(pipe) == TopPipe:
                screen.blit(textures.pipe_top, pipe.collision_model)
            else:
                screen.blit(textures.pipe_bottom, pipe.collision_model)

    def draw_score(self) -> None:
        score: Score = Score(self.container.score)
        screen.blit(score.texture, (Window.width // 2, 30))
