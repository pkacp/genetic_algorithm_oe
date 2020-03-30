import math

from src.BinaryChromosome import BinaryChromosome
from src.Evolution import Evolution
from src.Population import Population
from src.enums.SelectionType import SelectionType
from src.enums.CrossingType import CrossingType
from src.enums.MutationType import MutationType
from src.Individual import Individual
import time

if __name__ == '__main__':
    def sample_function(arg_arr):
        return 2 * ((arg_arr[0] - 1) * (arg_arr[0] - 1)) + 5


    def mccormick_function(arg_arr):
        return math.sin(arg_arr[0] + arg_arr[1]) + (arg_arr[0] - arg_arr[1]) * (arg_arr[0] - arg_arr[1]) - 1.5 * \
               arg_arr[0] + 2.5 * arg_arr[1] + 1.0


    # best working for now
    def levy_function(arg_arr):
        a = math.sin(3.0 * math.pi * arg_arr[0])
        b = math.sin(3.0 * math.pi * arg_arr[1])
        c = 1.0 + math.sin(2.0 * math.pi * arg_arr[1])
        return math.pow(a, 2) + math.pow(arg_arr[0] - 1.0, 2) * (1.0 + math.pow(b, 2)) + \
               math.pow(arg_arr[1] - 1.0, 2) * (1.0 + math.pow(c, 2))


    def bukin_function(arg_arr):
        return 100.0 * math.sqrt(math.fabs(arg_arr[1] - 0.01 * math.pow(arg_arr[0], 2))) + 0.01 * math.fabs(
            arg_arr[0] + 10.0)


    a = -10
    b = 10
    accuracy = 10
    epochs = 30
    number_of_chromosomes = 2
    population_size = 19
    k = 5  # tournament size

    evolution = Evolution(epochs, population_size, a, b, accuracy, levy_function, min, BinaryChromosome,
                          number_of_chromosomes, SelectionType.TOURNAMENT, [k], CrossingType.THREE_POINT, 0.9,
                          MutationType.TWO_POINT, 1, 2)
    evolution.run()

    # pop1 = Population(BinaryChromosome, population_size, number_of_chromosomes, 5, a, b, sample_function)
    #
    # pop1.show()
    # best = pop1.selection(SelectionType.BEST, 3, min)
    # print(best)
    # print(best)
    #
    # roulette = pop1.roulette_selection(2, min)
    #
    # i1 = Individual(BinaryChromosome, number_of_chromosomes, 6, a, b)
    # i2 = Individual(BinaryChromosome, number_of_chromosomes, 6, a, b)
    #
    # i1.show()
    #
    # print("-------------------------------------")
    # i1.mutate(MutationType.ONE_POINT)
    #
    # i1.show()
