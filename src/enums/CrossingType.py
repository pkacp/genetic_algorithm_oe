from enum import Enum

from src.BinaryChromosome import BinaryChromosome
from src.RealChromosome import RealChromosome


class CrossingType(Enum):
    # Types of crossovers probably should be in their owns classes
    ONE_POINT = BinaryChromosome.one_point_crossover
    TWO_POINT = BinaryChromosome.two_point_crossover
    THREE_POINT = BinaryChromosome.three_point_crossover

    ARITHMETIC = RealChromosome.arithmetic_crossover
    HEURISTIC = RealChromosome.heuristic_crossover
