from src.Chromosome import Chromosome
import numpy as np


class BinaryChromosome(Chromosome):
    def __init__(self, range_start, range_end, accuracy, value=np.array([False])):
        self.range_start = range_start
        self.range_end = range_end
        self.accuracy = accuracy
        self.number_of_genes = self.calculate_number_of_genes()
        if value.any():
            self.value = value
        else:
            self.value = self.randomize_value()

    def randomize_value(self):
        return np.random.randint(0, 2, size=self.number_of_genes)

    def show(self):
        print(self.value, end='')

    def decode_val_to_decimal(self) -> float:
        m = len(self.value)
        return self.range_start + self.__binary_arr_to_int(self.value) * (self.range_end - self.range_start) / (
                    pow(2, m) - 1)

    def calculate_number_of_genes(self):
        if self.range_start > self.range_end:
            raise ValueError('Wrong range')
        else:
            return np.math.ceil(np.math.log2(abs(self.range_end - self.range_start) * pow(10, self.accuracy)))

    @staticmethod
    def __binary_arr_to_int(binary_array) -> int:
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
        return BinaryChromosome(first_chromosome.range_start, first_chromosome.range_end, first_chromosome.accuracy,
                                new_first_chromosome_val), \
               BinaryChromosome(second_chromosome.range_start, second_chromosome.range_end, second_chromosome.accuracy,
                                new_second_chromosome_val)

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

    @staticmethod
    def reverse_bit(bit):
        return int(not bit)

    def n_bits_mutation(self, n, place):
        if n > self.number_of_genes:
            raise IndexError("More mutations than expected")
        if place == 'start':
            for i in range(n):
                self.value[i] = self.reverse_bit(self.value[i])
        elif place == 'end':
            for i in range(n):
                self.value[-i - 1] = self.reverse_bit(self.value[-i - 1])
        elif place == 'random':
            bits_to_change_indexes = np.random.choice(np.arange(self.number_of_genes), n, replace=False)
            for i in bits_to_change_indexes:
                self.value[i] = self.reverse_bit(self.value[i])
        else:
            raise TypeError("You can only mutate on start or end or in random place of chromosome")

    def inversion(self):
        inversion_places = np.sort(np.random.choice(self.number_of_genes, size=2, replace=False))
        for i in range(inversion_places[0], inversion_places[1]):
            self.value[i] = self.reverse_bit(self.value[i])
