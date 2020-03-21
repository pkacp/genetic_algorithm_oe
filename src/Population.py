import numpy as np

from src.Individual import Individual


class Population:
    def __init__(self, chromosome_type, pop_size, chr_num_in_indiv, genes_in_chr):
        self.size = pop_size
        self.individuals = self.generate_population(chromosome_type, chr_num_in_indiv, genes_in_chr)

    def generate_population(self, chromosome_type, chr_num_in_indiv, genes_in_chr):
        individuals = []
        for i in range(self.size):
            individuals.append(Individual(chromosome_type, chr_num_in_indiv, genes_in_chr))
        return np.asarray(individuals)

    def print_population(self):
        for individual in self.individuals:
            for chromosome in individual.chromosomes:
                chromosome.show()
            print(" ")

    def print_decimal_population(self, range_start, range_end):
        for individual in self.individuals:
            for chromosome in individual.chromosomes:
                print(chromosome.decode_val_to_decimal(range_start, range_end))
            print(" ")

