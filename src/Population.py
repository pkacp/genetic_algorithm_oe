import numpy as np

from src.Individual import Individual


class Population:
    def __init__(self, chromosome_type, pop_size, chr_num_in_indiv, genes_in_chr, range_start, range_end,
                 fitness_function, searching_value, crossover_type, elite_strategy_num, values=np.array([])):
        self.chromosome_type = chromosome_type
        self.size = pop_size
        self.chr_num_in_indiv = chr_num_in_indiv
        self.genes_in_chr = genes_in_chr
        self.range_start = range_start
        self.range_end = range_end
        self.fitness_function = fitness_function
        self.searching_value = searching_value
        self.crossover_type = crossover_type
        self.crossover_prob = 0.9
        # self.mutation_prob = 0.1
        # self.inversion_prob = 0.05
        self.elite_strategy_num = elite_strategy_num
        self.selected_individuals = np.array([])
        self._individuals = self.generate_population(values)
        self.evaluated_population = self.__evaluate_population()
        self.best_individuals = self.__elite_strategy()

    def generate_population(self, values):
        if values.any():  # TODO check if number of given individuals is correct
            return values
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

    def __evaluate_population(self):
        return self.evaluate_individuals(self._individuals, self.fitness_function)

    @staticmethod
    def evaluate_individuals(individuals_arr, fitness_function):
        individuals_eval = []
        for individual in individuals_arr:
            individuals_eval.append(individual.evaluate(fitness_function))
        return np.array((individuals_arr, np.asarray(individuals_eval))).T

    def __elite_strategy(self):
        return self.best_selection(self.elite_strategy_num, [])

    def get_best_individual(self):
        best_value = self.searching_value(self.evaluated_population[:, 1])
        print(best_value)
        return np.where(self.evaluated_population[1] == best_value)

    def select_individuals(self, selection_method, *args):
        num_individuals_to_select = self.size - self.elite_strategy_num
        self.selected_individuals = selection_method(self, num_individuals_to_select, args)

    def best_selection(self, num_of_individuals_to_select, args):
        sorted_evaluated_pop = self.evaluated_population[np.argsort(self.evaluated_population[:, 1])]
        # print("sorted_evaluated_pop")
        # print(sorted_evaluated_pop)
        if self.searching_value == max:
            return sorted_evaluated_pop[-num_of_individuals_to_select:][:, 0]
        elif self.searching_value == min:
            return sorted_evaluated_pop[:num_of_individuals_to_select][:, 0]
        else:
            raise TypeError("Searching only for minimum or maximum value")

    def roulette_selection(self, num_of_individuals_to_select, args):
        evaluated_pop = self.evaluated_population
        if self.searching_value == min:
            evaluated_pop[:, 1] = 1.0 / evaluated_pop[:, 1]
        sum_of_evaluated_individuals = np.sum(evaluated_pop[:, 1])
        individuals_probability = []
        for i in range(evaluated_pop.shape[0]):
            individuals_probability.append(evaluated_pop[i][1] / sum_of_evaluated_individuals)
        selected_individuals = np.random.choice(evaluated_pop[:, 0], num_of_individuals_to_select,
                                                p=individuals_probability)
        return selected_individuals

    def ranking_selection(self):
        return self._individuals[0]  # TODO ranking selection

    def tournament_selection(self):
        return self._individuals[0]  # TODO tournament selection

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
