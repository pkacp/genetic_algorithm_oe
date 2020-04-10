import numpy as np
from src.enums.MutationType import MutationType


class Individual:
    def __init__(self, chromosome_type, number_of_chromosomes, range_start, range_end, accuracy,
                 chr_values=np.array([False])):
        self.chromosome_type = chromosome_type
        self.number_of_chromosomes = number_of_chromosomes
        self.range_start = range_start
        self.range_end = range_end
        self.accuracy = accuracy
        if chr_values.any():
            self.chromosomes = chr_values
        else:
            self.chromosomes = self.__generate_chromosomes(chromosome_type)

    def show(self):
        for chromosome in self.chromosomes:
            chromosome.show()
        print("")

    def __generate_chromosomes(self, chromosome_type):
        chromosomes = []
        for i in range(self.number_of_chromosomes):
            chromosomes.append(chromosome_type(self.range_start, self.range_end, self.accuracy))
        return np.asarray(chromosomes)

    def crossover(self, crossover_type, other_individual):
        first_new_values = []
        second_new_values = []
        for i in range(self.number_of_chromosomes):
            first_new, second_new = crossover_type(self.chromosomes[i], other_individual.chromosomes[i])
            first_new_values.append(first_new)
            second_new_values.append(second_new)
        new_individual_1 = Individual(self.chromosome_type, self.number_of_chromosomes, self.range_start,
                                      self.range_end, self.accuracy, np.asarray(first_new_values))
        new_individual_2 = Individual(other_individual.chromosome_type, other_individual.number_of_chromosomes,
                                      other_individual.range_start, other_individual.range_end,
                                      other_individual.accuracy, np.asarray(second_new_values))
        return new_individual_1, new_individual_2

    def mutate(self, mutation_type):
        for chromosome in self.chromosomes:
            if mutation_type == MutationType.ONE_POINT:
                chromosome.n_bits_mutation(MutationType.ONE_POINT.value['n'], MutationType.ONE_POINT.value['place'])
            elif mutation_type == MutationType.TWO_POINT:
                chromosome.n_bits_mutation(MutationType.TWO_POINT.value['n'], MutationType.TWO_POINT.value['place'])
            elif mutation_type == MutationType.THREE_POINT:
                chromosome.n_bits_mutation(MutationType.THREE_POINT.value['n'], MutationType.THREE_POINT.value['place'])
            elif mutation_type == MutationType.BORDER:
                chromosome.n_bits_mutation(MutationType.BORDER.value['n'], MutationType.BORDER.value['place'])
            else:
                raise TypeError("Wrong mutation type")

    def invert(self):
        for chromosome in self.chromosomes:
            chromosome.inversion()

    def get_decimal_value_of_chromosomes(self):
        decimal_values = []
        for chromosome in self.chromosomes:
            decimal_values.append(chromosome.decode_val_to_decimal(self.range_start, self.range_end))
        return decimal_values

    def evaluate(self, fitness_function):
        return fitness_function(self.get_decimal_value_of_chromosomes())
