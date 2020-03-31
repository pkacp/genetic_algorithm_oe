from enum import Enum

from src.BinaryChromosome import BinaryChromosome


class CrossingType(Enum):
    ONE_POINT = BinaryChromosome.one_point_crossover
    TWO_POINT = BinaryChromosome.two_point_crossover
    THREE_POINT = BinaryChromosome.three_point_crossover
