import numpy as np


class Chromosome:
    def show(self):
        pass


class BinaryChromosome(Chromosome):
    @staticmethod
    def calculate_chain_length(range_start, range_end, acc):
        if range_start > range_end:
            return "Wrong range"
        else:
            return np.math.ceil(np.math.log2(abs(range_end - range_start) * pow(10, acc)))

    def __init__(self, genes_in_chr):
        self.value = np.random.randint(0, 2, size=genes_in_chr)

    def show(self):
        print(self.value)

    def decode_val_to_decimal(self):
        return self.value


class Individual:
    def __init__(self, chromosome_type, chr_in_indiv, genes_in_chr):
        chromosomes = []
        for i in range(chr_in_indiv):
            chromosomes.append(chromosome_type(genes_in_chr))
        self.chromosomes = np.asarray(chromosomes)


class Population:
    def __init__(self, chromosome_type, pop_size, chr_in_indiv, genes_in_chr):
        individuals = []
        for i in range(pop_size):
            individuals.append(Individual(chromosome_type, chr_in_indiv, genes_in_chr))
        self.individuals = np.asarray(individuals)

    def print_population(self):
        for individual in self.individuals:
            for chromosome in individual.chromosomes:
                chromosome.show()
            print(" ")


a = -10
b = 10
accuracy = 6

number_of_genes = BinaryChromosome.calculate_chain_length(a, b, accuracy)

chromosome_size = 1
population_size = 5

pop1 = Population(BinaryChromosome, population_size, chromosome_size, number_of_genes)
pop1.print_population()


epochs_number = 10
