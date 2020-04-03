import copy

import numpy as np

from src.Individual import Individual


class Population:
    def __init__(self, chromosome_type, pop_size, chr_num_in_indiv, genes_in_chr, range_start, range_end,
                 fitness_function, searching_value, crossover_type, crossover_prob, elite_strategy_num,
                 values=np.array([])):
        self.chromosome_type = chromosome_type
        self.size = pop_size
        self.chr_num_in_indiv = chr_num_in_indiv
        self.genes_in_chr = genes_in_chr
        self.range_start = range_start
        self.range_end = range_end
        self.fitness_function = fitness_function
        self.searching_value = searching_value
        self.crossover_type = crossover_type
        self.crossover_prob = crossover_prob
        self.elite_strategy_num = elite_strategy_num
        self.selected_individuals = np.array([])
        self._individuals = self.generate_population(values)
        self.best_individuals = self.__elite_strategy()
        self.evaluated_starting_individuals = self.evaluate_individuals(self._individuals, self.fitness_function)

    def generate_population(self, values):
        if values.shape[0] == self.size:
            return values
        elif values.any() and values.shape[0] < self.size:
            raise ValueError(f"Wrong number of individuals, expected{self.size}, get {values.shape[0]}")
        else:
            individuals = []
            for i in range(self.size):
                individuals.append(Individual(self.chromosome_type, self.chr_num_in_indiv, self.genes_in_chr,
                                              self.range_start, self.range_end))
            return np.asarray(individuals)

    def show(self):
        for individual in self._individuals:
            individual.show()

    def show_decimal(self):
        for individual in self._individuals:
            print(individual.get_decimal_value_of_chromosomes())

    @staticmethod
    def evaluate_individuals(individuals_arr, fitness_function):
        individuals_eval = []
        for individual in individuals_arr:
            individuals_eval.append(individual.evaluate(fitness_function))
        return np.array((individuals_arr, np.asarray(individuals_eval))).T

    def __elite_strategy(self):
        return self.get_n_best_individuals(self.elite_strategy_num, self.searching_value, self._individuals,
                                           self.fitness_function)

    def select_individuals(self, selection_method, args):
        self.selected_individuals = selection_method(self, args)

    def best_selection(self, args):
        num_of_individuals_to_select = args[0]
        return Population.get_n_best_individuals(num_of_individuals_to_select, self.searching_value,
                                                 self._individuals,
                                                 self.fitness_function)

    @staticmethod
    def get_n_best_individuals(number_to_select, values_to_select, individuals, fitness_function):
        evaluated_individuals = Population.evaluate_individuals(individuals, fitness_function)
        sorted_evaluated_individuals = evaluated_individuals[np.argsort(evaluated_individuals[:, 1])]
        if values_to_select == max:
            return sorted_evaluated_individuals[-number_to_select:][:, 0]
        elif values_to_select == min:
            return sorted_evaluated_individuals[:number_to_select][:, 0]
        else:
            raise TypeError("Searching only for minimum or maximum value")

    def roulette_selection(self, args):
        num_of_individuals_to_select = args[0]
        evaluated_pop = self.evaluate_individuals(self._individuals, self.fitness_function)
        if self.searching_value == min:
            evaluated_pop[:, 1] = 1.0 / evaluated_pop[:, 1]
        sum_of_evaluated_individuals = np.sum(evaluated_pop[:, 1])
        individuals_probability = []
        for i in range(evaluated_pop.shape[0]):
            individuals_probability.append(evaluated_pop[i][1] / sum_of_evaluated_individuals)
        # print(individuals_probability) # TODO working for negatives
        # if self.searching_value == min:
        #     individuals_probability = np.power(individuals_probability, 2)
        selected_individuals = np.random.choice(evaluated_pop[:, 0], num_of_individuals_to_select,
                                                p=individuals_probability)
        return selected_individuals

    def tournament_selection(self, args):
        selected_individuals = []
        tournament_size = args[0]
        tournaments_number = round(self.size / tournament_size)
        np.random.shuffle(self._individuals)
        tournaments = np.array_split(self._individuals, tournaments_number)
        for tournament in tournaments:
            selected_individuals.append(
                self.get_n_best_individuals(1, self.searching_value, tournament, self.fitness_function)[0])
        return np.asarray(selected_individuals)

    def crossover_selected_individuals(self):
        num_individuals_to_return = self.size - self.elite_strategy_num
        individuals_for_crossing = self.__pick_individuals_with_probability()
        new_individuals = self.__cross_every_picked_individual(individuals_for_crossing)
        num_missing_individuals = num_individuals_to_return - len(new_individuals)
        missing_individuals = []
        if num_missing_individuals > 0:
            missing_individuals = self.__cross_random_picked_individuals(num_missing_individuals,
                                                                         individuals_for_crossing)
        elif num_missing_individuals < 0:
            new_individuals.pop(num_missing_individuals)
        all_new_individuals = new_individuals + missing_individuals
        return np.asarray(all_new_individuals)

    def __pick_individuals_with_probability(self):
        individuals_for_crossing = []
        for individual in self.selected_individuals:
            if np.random.random_sample() < self.crossover_prob:
                individuals_for_crossing.append(individual)
        return individuals_for_crossing

    def __cross_every_picked_individual(self, individuals_for_crossing):
        individuals_split = np.array_split(individuals_for_crossing, 2)
        if len(individuals_split[0]) > len(individuals_split[1]):
            individuals_split[1] = np.append(individuals_split[1], individuals_split[0][0])
        new_individuals = []
        for i0, i1 in zip(individuals_split[0], individuals_split[1]):
            new_i0, new_i1 = i0.crossover(self.crossover_type, i1)
            new_individuals.append(new_i0)
            new_individuals.append(new_i1)
        return new_individuals

    def __cross_random_picked_individuals(self, number_to_fill, individuals_list):
        crossed_individuals = []
        for i in range(int(number_to_fill / 2)):
            individuals_to_cross = np.random.choice(individuals_list, 2)
            new_i0, new_i1 = individuals_to_cross[0].crossover(self.crossover_type, individuals_to_cross[1])
            crossed_individuals.append(new_i0)
            crossed_individuals.append(new_i1)
        if number_to_fill % 2 != 0:
            individuals_to_cross = np.random.choice(individuals_list, 2)
            new_i = individuals_to_cross[0].crossover(self.crossover_type, individuals_to_cross[1])
            crossed_individuals.append(new_i[0])
        return crossed_individuals

    @staticmethod
    def mutate_individuals(group_of_individuals, mutation_type, mutation_prob):
        for individual in group_of_individuals:
            if np.random.rand() < mutation_prob:
                individual.mutate(mutation_type)

    @staticmethod
    def inverse_individuals(group_of_individuals, inversion_prob):
        for individual in group_of_individuals:
            if np.random.rand() < inversion_prob:
                individual.invert()
