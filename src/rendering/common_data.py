from src.constants import GameConditionEnum
from src.models.background import Background
from src.models.pipes.abstract import AbstractPipe


class ItemContainer:
    bird_frame_num: int = 0
    backgrounds: list[Background] = [Background()]
    pipes: list[AbstractPipe] = []
    passed_pipes: set[AbstractPipe] = set()
    game_condition: GameConditionEnum = GameConditionEnum.start
    score: int | float = 0


item_container: ItemContainer = ItemContainer()
