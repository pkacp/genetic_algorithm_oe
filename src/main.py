import math

from src.BinaryChromosome import BinaryChromosome
from src.DataAnalyzer import DataAnalyzer
from src.Evolution import Evolution
from src.Functions import Functions
from src.enums.SelectionType import SelectionType
from src.enums.CrossingType import CrossingType
from src.enums.MutationType import MutationType

if __name__ == '__main__':
    pass
    # # parameters about evolution
    # epochs = 50
    # population_size = 1000
    # range_start = -10
    # range_end = 10
    # accuracy = 6
    # function = Functions.levy_function
    # searching_value = min
    # chromosome_type = BinaryChromosome
    # number_of_chromosomes = 2
    # selection_type = SelectionType.TOURNAMENT
    # selection_args = [10]  # depending from selection type(tournament size/number of individuals to pick)
    # crossing_type = CrossingType.ONE_POINT
    # crossing_prob = 0.9
    # mutation_type = MutationType.TWO_POINT
    # mutation_prob = 0.01
    # inversion_prob = 0.05
    # keeping_elite_num = 30
    #
    # evolution = Evolution(epochs, population_size, range_start, range_end, accuracy, function, searching_value,
    #                       chromosome_type, number_of_chromosomes, selection_type, selection_args, crossing_type,
    #                       crossing_prob, mutation_type, mutation_prob, inversion_prob, keeping_elite_num)
    # evolution.run()
    #
    # # parameters about plots
    # function_value_from_iteration = True
    # mean_function_value_from_iteration = True
    # sd_from_iteration = True
    #
    # print("_________________________________________")
    # DataAnalyzer(evolution, function_value_from_iteration, mean_function_value_from_iteration, sd_from_iteration)
    #
