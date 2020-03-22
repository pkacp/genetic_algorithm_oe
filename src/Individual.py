import numpy as np


class Individual:
    def __init__(self, chromosome_type, number_of_chromosomes, genes_in_chr, chr_values=np.array([False])):
        self.chromosome_type = chromosome_type
        self.number_of_chromosomes = number_of_chromosomes
        self.genes_in_chr = genes_in_chr
        if chr_values.any():
            self.chromosomes = chr_values
        else:
            self.chromosomes = self.__generate_chromosomes(chromosome_type, genes_in_chr)

    def show(self):
        for chromosome in self.chromosomes:
            chromosome.show()
        print("")

    def __generate_chromosomes(self, chromosome_type, genes_in_chr):
        chromosomes = []
        for i in range(self.number_of_chromosomes):
            chromosomes.append(chromosome_type(genes_in_chr))
        return np.asarray(chromosomes)

    def crossover(self, crossover_type, other_individual):
        # crossover type -> BinaryChromosome.(one/two/three)_point_crossover, BinaryChromosome.uniform_crossover
        first_new_values = []
        second_new_values = []
        for i in range(self.number_of_chromosomes):
            first_new, second_new = crossover_type(self.chromosomes[i], other_individual.chromosomes[i])
            first_new_values.append(first_new)
            second_new_values.append(second_new)
        new_individual_1 = Individual(self.chromosome_type, self.number_of_chromosomes, self.genes_in_chr,
                                      np.asarray(first_new_values))
        new_individual_2 = Individual(other_individual.chromosome_type, other_individual.number_of_chromosomes,
                                      other_individual.genes_in_chr, np.asarray(second_new_values))
        return new_individual_1, new_individual_2
