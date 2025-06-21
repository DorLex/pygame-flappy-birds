from enum import StrEnum
from pathlib import Path
from random import randint

BASE_DIR: Path = Path(__file__).resolve().parent.parent

textures_folder: Path = BASE_DIR / 'src/images'


class Window:
    width: int = 800
    height: int = 600  # == размеру текстуры background


class RandomPipeHeight:
    min: int = 100
    max: int = 300

    @classmethod
    def get(cls) -> int:
        return randint(cls.min, cls.max)


class GameConditionEnum(StrEnum):
    start = 'start'
    play = 'play'
