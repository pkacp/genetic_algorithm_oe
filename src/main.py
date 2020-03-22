from src.BinaryChromosome import BinaryChromosome
from src.Individual import Individual

if __name__ == '__main__':
    a = -10
    b = 10
    accuracy = 2

    number_of_genes = BinaryChromosome.calculate_chain_length(a, b, accuracy)

    number_of_chromosomes = 2
    population_size = 2

    # pop1 = Population(BinaryChromosome, population_size, chromosome_size, number_of_genes)
    # pop1.print_population()
    # pop1.print_decimal_population(a, b)

    # epochs_number = 10

    i1 = Individual(BinaryChromosome, number_of_chromosomes, number_of_genes)
    i2 = Individual(BinaryChromosome, number_of_chromosomes, number_of_genes)

    i1.show()
    i2.show()

    print("-------------------------------------")
    i3, i4 = i1.crossover(BinaryChromosome.one_point_crossover, i2)

    i3.show()
    i4.show()
