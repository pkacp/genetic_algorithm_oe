import numpy as np


class Individual:
    def __init__(self, chromosome_type, chr_num_in_indiv, genes_in_chr):
        chromosomes = []
        for i in range(chr_num_in_indiv):
            chromosomes.append(chromosome_type(genes_in_chr))
        self.chromosomes = np.asarray(chromosomes)
