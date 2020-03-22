import numpy as np
import random

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

    def best_selection(self, num_of_individuals_to_select, searching_value):
        evaluated_pop = self.__evaluate_population()
        sorted_evaluated_pop = evaluated_pop[np.argsort(evaluated_pop[:, 1])]
        if searching_value == max:
            return sorted_evaluated_pop[-num_of_individuals_to_select:][:, 0]
        elif searching_value == min:
            return sorted_evaluated_pop[:num_of_individuals_to_select][:, 0]
        else:
            raise TypeError("Searching only for minimum or maximum value")

    def roulette_selection(self, num_of_individuals_to_select, searching_value):
        evaluated_pop = self.__evaluate_population()
        if searching_value == min:
            evaluated_pop[:, 1] = 1.0 / evaluated_pop[:, 1]
        sum_of_evaluated_individuals = np.sum(evaluated_pop[:, 1])
        individuals_probability = []
        for i in range(evaluated_pop.shape[0]):
            individuals_probability.append(evaluated_pop[i][1] / sum_of_evaluated_individuals)
        individuals_cumsum = np.cumsum(np.asarray(individuals_probability))
        # eval_pop_with_prob = np.c_[evaluated_pop, np.asarray(individuals_probability)]
        # eval_pop_with_prob_cumsum = np.c_[eval_pop_with_prob, (np.cumsum(eval_pop_with_prob[:, 2]))]
        # print(eval_pop_with_prob_cumsum)
        print(individuals_probability)
        print(evaluated_pop)
        selected_individuals = np.random.choice(evaluated_pop[:, 0], num_of_individuals_to_select,
                                                p=individuals_probability)
        print(selected_individuals)
        # for i in range(num_of_individuals_to_select):
        #     random.random()
        #     for individual in range(eval_pop_with_prob_cumsum):
        #         individual[3]
        #     selected_individuals.append()
        return selected_individuals  # TODO return selected individuals
