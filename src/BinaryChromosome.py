from src.Chromosome import Chromosome
import numpy as np


class BinaryChromosome(Chromosome):
    def __init__(self, genes_in_chr, value=np.array([False])):
        self.number_of_genes = genes_in_chr
        if value.any():
            self.value = value
        else:
            self.value = self.randomize_value()

    def randomize_value(self):
        return np.random.randint(0, 2, size=self.number_of_genes)

    def show(self):
        print(self.value, end='')

    def decode_val_to_decimal(self, range_start, range_end) -> float:
        m = len(self.value)
        return range_start + self.binary_arr_to_int(self.value) * (range_end - range_start) / (pow(2, m) - 1)

    @staticmethod
    def calculate_chain_length(range_start, range_end, acc):
        if range_start > range_end:
            raise ValueError('Wrong range')
        else:
            return np.math.ceil(np.math.log2(abs(range_end - range_start) * pow(10, acc)))

    @staticmethod
    def binary_arr_to_int(binary_array) -> int:
        str_bit_number = ''
        for bit in list(binary_array):
            str_bit_number += (str(bit))
        return int(str_bit_number, 2)

    @staticmethod
    def __n_point_crossover(n, first_chromosome, second_chromosome):
        num_of_arr_to_get_after_split = n + 1
        self_split = np.array_split(first_chromosome.value, num_of_arr_to_get_after_split)
        other_split = np.array_split(second_chromosome.value, num_of_arr_to_get_after_split)
        self_array_of_splits = []
        other_array_of_splits = []
        for i in range(num_of_arr_to_get_after_split):
            if i % 2 == 0:
                self_array_of_splits.append(self_split[i])
                other_array_of_splits.append(other_split[i])
            else:
                self_array_of_splits.append(other_split[i])
                other_array_of_splits.append(self_split[i])
        new_first_chromosome_val = np.concatenate(self_array_of_splits)
        new_second_chromosome_val = np.concatenate(other_array_of_splits)
        return BinaryChromosome(first_chromosome.number_of_genes, new_first_chromosome_val), BinaryChromosome(
            second_chromosome.number_of_genes, new_second_chromosome_val)

    @staticmethod
    def one_point_crossover(first_chromosome, second_chromosome):
        return BinaryChromosome.__n_point_crossover(1, first_chromosome, second_chromosome)

    @staticmethod
    def two_point_crossover(first_chromosome, second_chromosome):
        return BinaryChromosome.__n_point_crossover(2, first_chromosome, second_chromosome)

    @staticmethod
    def three_point_crossover(first_chromosome, second_chromosome):
        return BinaryChromosome.__n_point_crossover(3, first_chromosome, second_chromosome)

    @staticmethod
    def uniform_crossover(first_chromosome, second_chromosome):
        return BinaryChromosome.__n_point_crossover(first_chromosome.number_of_genes - 1, first_chromosome,
                                                    second_chromosome)

    def border_mutation(self, place):
        if place == 'start':
            mutation_place = 0
        elif place == 'end':
            mutation_place = -1
        else:
            raise TypeError("You can only border mutate on start or end of chromosome")
        bit_value = self.value[mutation_place]
        if bit_value == 1:
            self.value[mutation_place] = 0
        elif bit_value == 0:
            self.value[mutation_place] = 1

    def inversion(self):
        return self.inversion_prob  # TODO implement inversion
