from enum import StrEnum
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent

textures_folder: Path = BASE_DIR / 'src/images'


class GameConditionEnum(StrEnum):
    start = 'start'
    play = 'play'
