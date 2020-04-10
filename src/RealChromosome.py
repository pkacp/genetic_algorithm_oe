import numpy as np

from src.Chromosome import Chromosome


class RealChromosome(Chromosome):
    def __init__(self, range_start, range_end, accuracy, value=None):
        self.range_start = range_start
        self.range_end = range_end
        self.accuracy = accuracy
        if value is not None:
            self.value = value
        else:
            self.value = self.randomize_value()

    def randomize_value(self):
        range_value = np.fabs(self.range_start - self.range_end)
        return np.random.rand()*range_value - np.fabs(self.range_start)

    def show(self):
        print(self.value)


