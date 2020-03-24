from enum import Enum

from src.Population import Population


class SelectionType(Enum):
    BEST = Population.best_selection
    ROULETTE = Population.roulette_selection
    RANKING = Population.ranking_selection
    TOURNAMENT = Population.tournament_selection

