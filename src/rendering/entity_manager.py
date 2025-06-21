from src.constants import GameConditionEnum, RandomPipeHeight, Window
from src.models.background import Background
from src.models.bird import bird
from src.models.pipes.abstract import BasePipe
from src.models.pipes.bottom import BottomPipe
from src.models.pipes.top import TopPipe
from src.rendering.common_data import EntityContainer
from src.settings import DISTANCE_FOR_SPAWN_NEW_PIPE


class EntityManager:
    def __init__(self, container: EntityContainer) -> None:
        self.container = container

    def spawn_background(self) -> None:
        right_side_last_background: int = self.container.backgrounds[-1].right
        if right_side_last_background <= Window.width:
            self.container.backgrounds.append(Background(x=right_side_last_background))

    def move_background(self) -> None:
        for background in self.container.backgrounds:
            background.x -= 1

            if background.right < 0:  # когда background за границами окна
                self._remove_background(background)

    def _remove_background(self, background: Background) -> None:
        self.container.backgrounds.remove(background)

    def spawn_pipes(self) -> None:
        if not self.container.pipes or self.container.pipes[-1].x < DISTANCE_FOR_SPAWN_NEW_PIPE:
            random_pipe_height: int = RandomPipeHeight.get()
            self.container.pipes.append(TopPipe(random_pipe_height))
            self.container.pipes.append(BottomPipe(random_pipe_height))

    def move_pipes(self) -> None:
        for pipe in self.container.pipes:
            pipe.x -= 5

            if pipe.right < -200:  # когда труба за границами окна
                self._remove_pipe(pipe)

    def _remove_pipe(self, pipe: BasePipe) -> None:
        self.container.pipes.remove(pipe)
        if pipe in self.container.passed_pipes:
            self.container.passed_pipes.remove(pipe)

    def bird_gravity(self) -> None:
        bird.fall_speed += 1
        bird.y += bird.fall_speed

    def check_collisions(self) -> None:
        # Столкновение с границами окна:
        if bird.bottom >= Window.height or bird.top <= 0:
            self._game_over()
            return

        # Столкновение с трубами:
        for pipe in self.container.pipes:
            if bird.colliderect(pipe):
                self._game_over()

    def increase_score(self) -> None:
        for pipe in self.container.pipes:
            if pipe.right <= bird.left and pipe not in self.container.passed_pipes:
                self.container.passed_pipes.add(pipe)
                self.container.score.value += 0.5

    def _game_over(self) -> None:
        self.container.game_condition = GameConditionEnum.start
        self.container.score.value = 0
        self.container.pipes = []
        self.container.passed_pipes = set()
        bird.y = bird.base_y
