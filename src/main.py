from src.BinaryChromosome import BinaryChromosome
from src.Population import Population

if __name__ == '__main__':
    a = -10
    b = 10
    accuracy = 6

    number_of_genes = BinaryChromosome.calculate_chain_length(a, b, accuracy)

    chromosome_size = 1
    population_size = 5

    pop1 = Population(BinaryChromosome, population_size, chromosome_size, number_of_genes)
    pop1.print_population()
    pop1.print_decimal_population(a, b)

    epochs_number = 10
    #
    # aa = BinaryChromosome(7)
    # bb = BinaryChromosome(7)
    # aa.show()
    # bb.show()
    #
    # # aa.two_point_cross(bb)
    # aa.n_point_cross(4, bb)
    # aa.show()
    # bb.show()
