from src.Chromosome import Chromosome
import numpy as np


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
        print(np.array2string(self.value).__class__)
