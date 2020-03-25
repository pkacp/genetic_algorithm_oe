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
        return 2 * (arg_arr[0] * arg_arr[0]) + 5


    a = -10
    b = 10
    accuracy = 6
    epochs = 30
    number_of_chromosomes = 1
    population_size = 500

    # evolution = Evolution(epochs, population_size, a, b, accuracy, sample_function, min, BinaryChromosome,
    #                       number_of_chromosomes, SelectionType.ROULETTE, (), CrossingType.THREE_POINT, 0.9, None, 0, 100)
    # evolution.run()

    # pop1 = Population(BinaryChromosome, population_size, number_of_chromosomes, 5, a, b, sample_function)
    #
    # pop1.show()
    # best = pop1.selection(SelectionType.BEST, 3, min)
    # print(best)
    # print(best)
    #
    # roulette = pop1.roulette_selection(2, min)
    #
    i1 = Individual(BinaryChromosome, number_of_chromosomes, 6, a, b)
    i2 = Individual(BinaryChromosome, number_of_chromosomes, 6, a, b)

    i1.show()

    print("-------------------------------------")
    i1.mutation(MutationType.ONE_POINT)

    i1.show()


