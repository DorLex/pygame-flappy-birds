from src.constants import GameConditionEnum, RandomPipeHeight, Window
from src.models.background import Background
from src.models.bird import bird
from src.models.pipes.abstract import AbstractPipe
from src.models.pipes.bottom import BottomPipe
from src.models.pipes.top import TopPipe
from src.rendering.common_data import EntityContainer
from src.settings import DISTANCE_FOR_SPAWN_NEW_PIPE


class EntityManager:
    def __init__(self, container: EntityContainer) -> None:
        self.container = container

    def _game_over(self) -> None:
        self.container.game_condition = GameConditionEnum.start
        self.container.score = 0
        self.container.pipes = []
        bird.collision_model.y = bird.base_y

    def check_collisions(self) -> None:
        # Столкновение с границами окна:
        if bird.collision_model.bottom >= Window.height or bird.collision_model.top <= 0:
            self._game_over()
            return

        # Столкновение с трубами:
        for pipe in self.container.pipes:
            if bird.collision_model.colliderect(pipe.collision_model):
                self._game_over()

    def increase_score(self) -> None:
        for pipe in self.container.pipes:
            if pipe.collision_model.right <= bird.collision_model.left and pipe not in self.container.passed_pipes:
                self.container.passed_pipes.add(pipe)
                self.container.score += 0.5

    def pipes_spawn(self) -> None:
        if not self.container.pipes or self.container.pipes[-1].collision_model.x < DISTANCE_FOR_SPAWN_NEW_PIPE:
            random_pipe_height: int = RandomPipeHeight.get()
            self.container.pipes.append(TopPipe(random_pipe_height))
            self.container.pipes.append(BottomPipe(random_pipe_height))

    def _pipe_remove(self, pipe: AbstractPipe) -> None:
        self.container.pipes.remove(pipe)
        if pipe in self.container.passed_pipes:
            self.container.passed_pipes.remove(pipe)

    def pipes_movement(self) -> None:
        for pipe in self.container.pipes:
            pipe.collision_model.x -= 5

            if pipe.collision_model.right < -200:  # когда труба за границами окна
                self._pipe_remove(pipe)

    def background_spawn(self) -> None:
        if self.container.backgrounds[-1].collision_model.right <= Window.width:
            self.container.backgrounds.append(
                Background(x=self.container.backgrounds[-1].collision_model.right),
            )

    def _background_remove(self, background: Background) -> None:
        self.container.backgrounds.remove(background)

    def background_movement(self) -> None:
        for background in self.container.backgrounds:
            background.collision_model.x -= 1

            if background.collision_model.right < 0:  # когда background за границами окна
                self._background_remove(background)

    def bird_falling(self) -> None:
        bird.fall_speed += 1
        bird.collision_model.y += bird.fall_speed
