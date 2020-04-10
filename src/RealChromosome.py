import numpy as np

from src.Chromosome import Chromosome


class RealChromosome(Chromosome):
    def __init__(self, range_start, range_end, accuracy=None, value=None):
        self.range_start = range_start
        self.range_end = range_end
        self.accuracy = accuracy
        if value is not None:
            self.value = value
        else:
            self.value = self.randomize_value()

    def randomize_value(self):
        range_value = np.fabs(self.range_start - self.range_end)
        return np.random.rand() * range_value - np.fabs(self.range_start)

    def show(self):
        print(self.value, end='')

    def decode_val_to_decimal(self):
        return self.value

    @staticmethod
    def arithmetic_crossover(first_chromosome, second_chromosome):
        k = np.random.rand()
        new_first_chromosome_val = k * first_chromosome.value + (1 - k) * second_chromosome.value
        new_second_chromosome_val = (1 - k) * first_chromosome.value + k * second_chromosome.value
        return RealChromosome(first_chromosome.range_start, first_chromosome.range_end, value=new_first_chromosome_val), \
               RealChromosome(second_chromosome.range_start, second_chromosome.range_end,
                              value=new_second_chromosome_val)

    @staticmethod
    def heuristic_crossover(first_chromosome, second_chromosome):
        k = np.random.rand()
        new_first_chromosome_val = k * (first_chromosome.value - second_chromosome.value) + first_chromosome.value
        return RealChromosome(first_chromosome.range_start, first_chromosome.range_end,
                              value=new_first_chromosome_val), None

    def even_mutation(self):
        self.value = self.randomize_value()
