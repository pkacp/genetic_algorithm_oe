import numpy as np

from src.Individual import Individual


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
                # chromosome.decode_val_to_decimal()
            print(" ")
