from enum import StrEnum
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent

textures_folder: Path = BASE_DIR / 'src/images'


class Window:
    width: int = 800
    height: int = 600


class GameConditionEnum(StrEnum):
    start = 'start'
    play = 'play'
