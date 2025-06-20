from pygame import Rect

from src.constants import GameConditionEnum
from src.models.pipes.abstract import AbstractPipe


class DataContainer:
    def __init__(self) -> None:
        self.bird_frame_num = 0
        self.backgrounds: list[Rect] = [Rect(0, 0, 288, 600)]
        self.pipes: list[AbstractPipe] = []
        self.pipes_to_left_of_bird = []
        self.game_condition: GameConditionEnum = GameConditionEnum.start
        self.score = 0
