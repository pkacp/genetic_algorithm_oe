from src.BinaryChromosome import BinaryChromosome
from src.Population import Population
import time

if __name__ == '__main__':
    def sample_function(arg_arr):
        return 2 * (arg_arr[0] * arg_arr[0]) + 5

    a = -10
    b = 10
    accuracy = 2

    number_of_genes = BinaryChromosome.calculate_chain_length(a, b, accuracy)

    number_of_chromosomes = 1
    population_size = 5

    pop1 = Population(BinaryChromosome, population_size, number_of_chromosomes, number_of_genes, a, b, sample_function)
    best = pop1.best_selection(2)
    print(best)

    # i1 = Individual(BinaryChromosome, number_of_chromosomes, number_of_genes, a, b)
    # i2 = Individual(BinaryChromosome, number_of_chromosomes, number_of_genes, a, b)
    #
    # i1.show()
    # i2.show()
    #
    # print("-------------------------------------")
    # i3, i4 = i1.crossover(BinaryChromosome.one_point_crossover, i2)
    #
    # i3.show()
    # i4.show()
