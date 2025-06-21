from src.constants import GameConditionEnum
from src.models.background import Background
from src.models.pipes.abstract import BasePipe
from src.models.score import Score


class EntityContainer:
    backgrounds: list[Background] = [Background()]
    pipes: list[BasePipe] = []
    passed_pipes: set[BasePipe] = set()
    game_condition: GameConditionEnum = GameConditionEnum.start
    score: Score = Score()


entity_container: EntityContainer = EntityContainer()
