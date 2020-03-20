import numpy as np


class Chromosome:
    def __init__(self, number_of_genes):
        self.value = np.random.randint(0, 2, size=number_of_genes)


class Individual:
    def __init__(self, chromosomes_array):
        self.value = np.asarray(chromosomes_array)

    def decode_to_decimal(self):
        return 0 # TODO

class Population:
    def __init__(self, array_of_individuals):
        self.value = np.asarray(array_of_individuals)

    def print(self):
        for ind_val in self.value:
            for chr_val in ind_val.value:
                print(chr_val.value)
            print(" ")


def calculate_chain_length(range_start, range_end, acc):
    if range_start > range_end:
        print("Wrong range")
    else:
        return np.math.ceil(np.math.log2(abs(range_end - range_start) * pow(10, acc)))


def generate_population(number_of_genes, chromosome_size, population_size):
    population = []
    for i in range(population_size):
        chromosomes = []
        for j in range(chromosome_size):
            chromosomes.append(Chromosome(number_of_genes))
        population.append(Individual(chromosomes))
    return Population(population)


a = -10
b = 10
accuracy = 6

number_of_genes = calculate_chain_length(a, b, accuracy)

chromosome_size = 1
population_size = 5

pop1 = generate_population(number_of_genes, chromosome_size, population_size)
pop1.print()

epochs_number = 10




