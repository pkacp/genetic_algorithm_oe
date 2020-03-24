import numpy as np

from src.Individual import Individual


class Population:
    def __init__(self, chromosome_type, pop_size, chr_num_in_indiv, genes_in_chr, range_start, range_end,
                 fitness_function, searching_value, elite_strategy_num, values=np.array([])):
        self.size = pop_size
        self.fitness_function = fitness_function
        self.searching_value = searching_value
        # self.crossover_prob = 0.999
        # self.mutation_prob = 0.1
        # self.inversion_prob = 0.05
        self.best_individuals = np.array([])
        self.elite_strategy_num = elite_strategy_num
        self.selected_individuals  # TODO as field in population
        if values.any():
            self.individuals = values
        else:
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
            individuals_eval.append(individual.evaluate(self.fitness_function))
        return np.array((self.individuals, np.asarray(individuals_eval))).T

    def elite_strategy(self):
        self.best_individuals = self.best_selection(self.elite_strategy_num, self.searching_value, [])

    def selection(self, selection_method, num_individuals_to_select, searching_value, *args):
        return selection_method(self, num_individuals_to_select, searching_value, args)

    # evaluated_pop may be passed as argument after picking best in elite strategy
    def best_selection(self, num_of_individuals_to_select, searching_value, args):
        # num_of_individuals_to_select, searching_value = args[0], args[1]
        evaluated_pop = self.__evaluate_population()
        sorted_evaluated_pop = evaluated_pop[np.argsort(evaluated_pop[:, 1])]
        if searching_value == max:
            return sorted_evaluated_pop[-num_of_individuals_to_select:][:, 0]
        elif searching_value == min:
            return sorted_evaluated_pop[:num_of_individuals_to_select][:, 0]
        else:
            raise TypeError("Searching only for minimum or maximum value")

    def roulette_selection(self, num_of_individuals_to_select, searching_value, args):
        evaluated_pop = self.__evaluate_population()
        if searching_value == min:
            evaluated_pop[:, 1] = 1.0 / evaluated_pop[:, 1]
        sum_of_evaluated_individuals = np.sum(evaluated_pop[:, 1])
        individuals_probability = []
        for i in range(evaluated_pop.shape[0]):
            individuals_probability.append(evaluated_pop[i][1] / sum_of_evaluated_individuals)
        selected_individuals = np.random.choice(evaluated_pop[:, 0], num_of_individuals_to_select,
                                                p=individuals_probability)
        return selected_individuals

    def ranking_selection(self):
        return self.individuals[0]  # TODO ranking selection

    def tournament_selection(self):
        return self.individuals[0]  # TODO tournament selection
