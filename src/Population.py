import numpy as np

from src.Individual import Individual


class Population:
    def __init__(self, chromosome_type, pop_size, chr_num_in_indiv, genes_in_chr, range_start, range_end,
                 target_function):
        self.size = pop_size
        self.target_function = target_function
        self.individuals = self.generate_population(chromosome_type, chr_num_in_indiv, genes_in_chr, range_start,
                                                    range_end)

    def generate_population(self, chromosome_type, chr_num_in_indiv, genes_in_chr, range_start, range_end):
        individuals = []
        for i in range(self.size):
            individuals.append(Individual(chromosome_type, chr_num_in_indiv, genes_in_chr, range_start, range_end))
        return np.asarray(individuals)

    def show(self):
        for individual in self.individuals:
            individual.show()

    def show_decimal(self):
        for individual in self.individuals:
            print(individual.get_decimal_value_of_chromosomes())

    def __evaluate_population(self):
        individuals_eval = []
        for individual in self.individuals:
            individuals_eval.append(individual.evaluate(self.target_function))
        return np.array((self.individuals, np.asarray(individuals_eval))).T

    def best_selection(self, number_to_select, searching_value):
        evaluated_pop = self.__evaluate_population()
        print(evaluated_pop)
        sorted_evaluated_pop = evaluated_pop[np.argsort(evaluated_pop[:, 1])]
        print(sorted_evaluated_pop)
        if searching_value == max:
            return sorted_evaluated_pop[-number_to_select:]
        elif searching_value == min:
            return sorted_evaluated_pop[:number_to_select]
        else:
            raise TypeError("Searching only for minimum or maximum value")

    def roulette_selection(self, number_to_select):
        return 0  # TODO return selected individuals