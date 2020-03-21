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
        self.value = np.random.randint(0, 2, size=genes_in_chr)

    def show(self):
        print(self.value)

    def decode_val_to_decimal(self, range_start, range_end) -> float:
        m = len(self.value)
        return range_start + self.binary_arr_to_int(self.value) * (range_end - range_start) / (pow(2, m) - 1)
