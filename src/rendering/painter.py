from pygame import Surface
from pygame.transform import rotate

from src import textures
from src.components import screen
from src.constants import GameConditionEnum
from src.models.bird import bird
from src.models.pipes.top import TopPipe
from src.rendering.common_data import EntityContainer


class Painter:
    def __init__(self, container: EntityContainer) -> None:
        self.container = container

    def draw_background(self) -> None:
        for background in self.container.backgrounds:
            screen.blit(textures.background, background)

    def draw_bird(self) -> None:
        bird.frame_num = (bird.frame_num + 0.2) % 4
        bird_frame_texture: Surface = textures.bird_frames.subsurface(
            bird.width * int(bird.frame_num),
            0,
            bird.width,
            bird.height,
        )

        if self.container.game_condition == GameConditionEnum.play:
            bird_frame_texture: Surface = rotate(bird_frame_texture, -bird.fall_speed * 3)

        screen.blit(bird_frame_texture, bird)

    def draw_pipes(self) -> None:
        for pipe in self.container.pipes:
            if type(pipe) == TopPipe:
                screen.blit(textures.pipe_top, pipe)
            else:
                screen.blit(textures.pipe_bottom, pipe)

    def draw_score(self) -> None:
        screen.blit(self.container.score.texture, self.container.score.location)
