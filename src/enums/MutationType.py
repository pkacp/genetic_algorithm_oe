from enum import Enum


class MutationType(Enum):
    ONE_POINT = {'place': 'random', 'n': 1}
    TWO_POINT = {'place': 'random', 'n': 2}
    THREE_POINT = {'place': 'random', 'n': 3}
    BORDER = {'place': 'start', 'n': 1}
    EVEN = {}
    INDEX_CHANGE = {}
