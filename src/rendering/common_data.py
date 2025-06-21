from src.constants import GameConditionEnum
from src.models.background import Background
from src.models.pipes.abstract import BasePipe
from src.models.score import Score


class EntityContainer:
    def __init__(self) -> None:
        self.bird_frame_num: int = 0
        self.backgrounds: list[Background] = [Background()]
        self.pipes: list[BasePipe] = []
        self.passed_pipes: set[BasePipe] = set()
        self.game_condition: GameConditionEnum = GameConditionEnum.start
        self.score: Score = Score()


entity_container: EntityContainer = EntityContainer()
