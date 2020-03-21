from src.Chromosome import Chromosome
import numpy as np


class BinaryChromosome(Chromosome):
    @staticmethod
    def calculate_chain_length(range_start, range_end, acc):
        if range_start > range_end:
            return "Wrong range"
        else:
            return np.math.ceil(np.math.log2(abs(range_end - range_start) * pow(10, acc)))

    @staticmethod
    def binary_arr_to_int(binary_array) -> int:
        str_bit_number = ''
        for bit in list(binary_array):
            str_bit_number += (str(bit))
        return int(str_bit_number, 2)

    def __init__(self, genes_in_chr):
        # self.value = np.random.randint(0, 2, size=genes_in_chr)
        self.value = np.random.randint(0, 9, size=genes_in_chr)

    def show(self):
        print(self.value)

    def decode_val_to_decimal(self, range_start, range_end) -> float:
        m = len(self.value)
        return range_start + self.binary_arr_to_int(self.value) * (range_end - range_start) / (pow(2, m) - 1)

    def n_point_cross(self, n, other_binary_chromosome):
        self_split = np.array_split(self.value, n)
        other_split = np.array_split(other_binary_chromosome.value, n)
        print("-------------------")
        print(self_split)
        print(other_split)
        self_array_of_splits = []
        other_array_of_splits = []
        print("...............")
        for i in range(n):
            if i % 2 == 0:
                self_array_of_splits.append(self_split[i])
                other_array_of_splits.append(other_split[i])
            else:
                self_array_of_splits.append(other_split[i])
                other_array_of_splits.append(self_split[i])

        print(self_array_of_splits)
        print(other_array_of_splits)
        print("-------------------")
        self.value = np.concatenate(self_array_of_splits)
        other_binary_chromosome.value = np.concatenate(other_array_of_splits)

    # def one_point_cross(self, other_binary_chromosome):
    #     self_split = np.array_split(self.value, 2)
    #     other_split = np.array_split(other_binary_chromosome.value, 2)
    #     self.value = np.concatenate((self_split[0], other_split[1]))
    #     other_binary_chromosome.value = np.concatenate((other_split[0], self_split[1]))
    #
    # def two_point_cross(self, other_binary_chromosome):
    #     self_split = np.array_split(self.value, 3)
    #     other_split = np.array_split(other_binary_chromosome.value, 3)
    #     self.value = np.concatenate((self_split[0], other_split[1], self_split[2]))
    #     other_binary_chromosome.value = np.concatenate((other_split[0], self_split[1], other_split[2]))