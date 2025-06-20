from pygame import Rect

from src.constants import GameConditionEnum
from src.models.pipes.abstract import AbstractPipe


class ItemContainer:
    bird_frame_num: int = 0
    backgrounds: list[Rect] = [Rect(0, 0, 288, 600)]
    pipes: list[AbstractPipe] = []
    passed_pipes: set[AbstractPipe] = set()
    game_condition: GameConditionEnum = GameConditionEnum.start
    score: int | float = 0


item_container: ItemContainer = ItemContainer()
