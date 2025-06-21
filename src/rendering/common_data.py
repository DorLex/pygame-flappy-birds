from src.constants import GameConditionEnum
from src.models.background import Background
from src.models.pipes.abstract import BasePipe


class EntityContainer:
    bird_frame_num: int = 0
    backgrounds: list[Background] = [Background()]
    pipes: list[BasePipe] = []
    passed_pipes: set[BasePipe] = set()
    game_condition: GameConditionEnum = GameConditionEnum.start
    score: int | float = 0


entity_container: EntityContainer = EntityContainer()
