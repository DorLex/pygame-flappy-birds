import pygame

from src import textures
from src.components import screen
from src.constants import GameConditionEnum, Window
from src.models.bird import bird
from src.models.pipes.top import TopPipe
from src.models.score import Score
from src.rendering.common_data import DataContainer


class Painter:
    def __init__(self, container: DataContainer) -> None:
        self.container = container

    def draw_background(self) -> None:
        for bg_rect in self.container.backgrounds:
            screen.blit(textures.background_img_block, bg_rect)

    def draw_bird(self) -> None:
        self.container.bird_frame_num = (self.container.bird_frame_num + 0.2) % 4
        img_bird = textures.bird_frames.subsurface(
            bird.width * int(self.container.bird_frame_num),
            0,
            bird.width,
            bird.height,
        )

        if self.container.game_condition == GameConditionEnum.play:
            img_bird = pygame.transform.rotate(img_bird, -bird.fall_speed * 3)

        screen.blit(img_bird, bird.collision_model)

    def draw_pipes(self) -> None:
        for pipe in self.container.pipes:
            if type(pipe) == TopPipe:
                rect = textures.pipe_top.get_rect(bottomleft=pipe.collision_model.bottomleft)
                screen.blit(textures.pipe_top, rect)
            else:
                rect = textures.pipe_bottom.get_rect(topleft=pipe.collision_model.topleft)
                screen.blit(textures.pipe_bottom, rect)

    def draw_score(self) -> None:
        score: Score = Score(self.container.score)
        screen.blit(score.text, (Window.width // 2, 30))
