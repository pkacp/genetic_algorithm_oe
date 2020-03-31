import math

from src.BinaryChromosome import BinaryChromosome
from src.DataAnalyzer import DataAnalyzer
from src.Evolution import Evolution
from src.Population import Population
from src.enums.SelectionType import SelectionType
from src.enums.CrossingType import CrossingType
from src.enums.MutationType import MutationType
from src.Individual import Individual
import time

if __name__ == '__main__':
    def sample_function(arg_arr):
        return 2 * (arg_arr[0] * arg_arr[0]) + 5


    # prefered range x1 = [-1.5, 4] x2 = [-3,4] min: f(-0.54719, -1.54719) = -1.9133
    def mccormick_function(arg_arr):
        return math.sin(arg_arr[0] + arg_arr[1]) + (arg_arr[0] - arg_arr[1]) * (arg_arr[0] - arg_arr[1]) - 1.5 * \
               arg_arr[0] + 2.5 * arg_arr[1] + 1.0


    # best working for now
    # prefered range = [-10, 10] min: f(1, 1) = 0
    def levy_function(arg_arr):
        # print(arg_arr[0])
        a = math.sin(3.0 * math.pi * arg_arr[0])
        b = math.sin(3.0 * math.pi * arg_arr[1])
        c = 1.0 + math.sin(2.0 * math.pi * arg_arr[1])
        return math.pow(a, 2) + math.pow(arg_arr[0] - 1.0, 2) * (1.0 + math.pow(b, 2)) + \
               math.pow(arg_arr[1] - 1.0, 2) * (1.0 + math.pow(c, 2))


    # prefered range x1 = [-15, -5] x2 = [-3, 3] min: f(-10, 1) = 0
    def bukin_function(arg_arr):
        return 100.0 * math.sqrt(math.fabs(arg_arr[1] - 0.01 * math.pow(arg_arr[0], 2))) + 0.01 * math.fabs(
            arg_arr[0] + 10.0)


    # d= 2, m = 10, prefered range x = [0, 4] min: f(2.20, 1.57) = -1.8013
    def michalewicz_function(arg_arr):
        return -1.0 * (michalewicz_sum_element(arg_arr[0], 1) + michalewicz_sum_element(arg_arr[1], 2))


    def michalewicz_sum_element(x, i):
        return math.sin(x) * math.pow(math.sin(x * x * i), 20) / math.pi


    # parameters about evolution
    epochs = 50
    population_size = 1000
    range_start = -10
    range_end = 10
    accuracy = 6
    function = levy_function
    searching_value = min
    chromosome_type = BinaryChromosome
    number_of_chromosomes = 2
    selection_type = SelectionType.TOURNAMENT
    selection_args = [10]  # depending from selection type(tournament size/number of individuals to pick)
    crossing_type = CrossingType.ONE_POINT
    crossing_prob = 0.9
    mutation_type = MutationType.TWO_POINT
    mutation_prob = 0.1
    inversion_prob = 0.05
    keeping_elite_num = 30

    evolution = Evolution(epochs, population_size, range_start, range_end, accuracy, function, searching_value,
                          chromosome_type, number_of_chromosomes, selection_type, selection_args, crossing_type,
                          crossing_prob, mutation_type, mutation_prob, inversion_prob, keeping_elite_num)
    evolution.run()

    # parameters about plots
    function_value_from_iteration = True
    mean_function_value_from_iteration = True
    sd_from_iteration = True

    print("_________________________________________")
    DataAnalyzer(evolution, function_value_from_iteration, mean_function_value_from_iteration, sd_from_iteration)