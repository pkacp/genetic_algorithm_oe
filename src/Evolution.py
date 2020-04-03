import copy

import numpy as np
import time

from src.Population import Population


class Evolution:
    def __init__(self, epochs_num, population_size, range_start, range_end, accuracy, fitness_function, searching_value,
                 chromosome_type, chromosomes_number, selection_type, selection_args, crossover_type, crossover_prob,
                 mutation_type, mutation_prob, inversion_prob, elite_strategy_num=0):
        self.epochs_num = epochs_num
        self.population_size = population_size
        self.population_set = set()
        self.elite_strategy_num = elite_strategy_num
        self.range_start = range_start
        self.range_end = range_end
        self.fitness_function = fitness_function
        self.searching_value = searching_value
        self.chromosome_type = chromosome_type
        self.chromosomes_number = chromosomes_number
        self.selection_type = selection_type
        self.selection_args = selection_args
        self.crossover_type = crossover_type
        self.crossover_prob = crossover_prob
        self.mutation_type = mutation_type
        self.mutation_prob = mutation_prob
        self.inversion_prob = inversion_prob
        self.best_individuals = np.array([])
        self.number_of_genes = chromosome_type.calculate_chain_length(range_start, range_end, accuracy)
        self.time = 9999999999
        self.best_individual = None
        self.best_individual_generation = self.epochs_num
        self.bests_values = []
        self.mean_values = []
        self.sd_values = []

    def run(self):
        time_start = time.time()
        next_generation_individuals = np.array([False])
        for generation in range(self.epochs_num):
            new_population = Population(self.chromosome_type, self.population_size, self.chromosomes_number,
                                        self.number_of_genes, self.range_start, self.range_end, self.fitness_function,
                                        self.searching_value, self.crossover_type, self.crossover_prob,
                                        self.elite_strategy_num,
                                        next_generation_individuals)
            self.population_set.add(new_population)
            if self.elite_strategy_num > 0:
                self.best_individuals = self.elite_strategy(new_population.best_individuals)
            new_population.select_individuals(self.selection_type, self.selection_args)
            new_individuals = new_population.crossover_selected_individuals()
            if self.mutation_prob > 0.0:
                Population.mutate_individuals(new_individuals, self.mutation_type, self.mutation_prob)
            if self.inversion_prob > 0.0:
                Population.inverse_individuals(new_individuals, self.inversion_prob)
            if self.elite_strategy_num > 0:
                next_generation_individuals = np.append(new_individuals, self.best_individuals)
            else:
                next_generation_individuals = new_individuals
            self.fill_values_for_charts(next_generation_individuals, generation)

        best = Population.get_n_best_individuals(1, self.searching_value, next_generation_individuals,
                                                 self.fitness_function)
        self.best_individual = best[0]
        time_end = time.time()
        self.time = time_end - time_start

        print("Final best:")
        print(best[0].get_decimal_value_of_chromosomes())
        print("value:")
        print(best[0].evaluate(self.fitness_function))
        print("evolution time: ")
        print(self.time)
        print("BESTS")
        print(self.bests_values)
        print("MEAN")
        print(self.mean_values)
        print("STD")
        print(self.sd_values)

    def elite_strategy(self, new_best_candidates):
        individuals = np.asarray(list(set(np.append(self.best_individuals, new_best_candidates))))
        return Population.get_n_best_individuals(self.elite_strategy_num, self.searching_value, individuals,
                                                 self.fitness_function)

    def fill_values_for_charts(self, individuals, generation_number):
        evaluated_values = Population.evaluate_individuals(individuals, self.fitness_function)[:, 1]
        best_val = np.min(evaluated_values)
        if generation_number > 0 and self.elite_strategy_num > 0:
            if best_val < self.searching_value(self.bests_values):
                self.best_individual_generation = generation_number
        self.bests_values.append(best_val)
        self.mean_values.append(np.mean(evaluated_values))
        self.sd_values.append(np.std(evaluated_values))

    def to_string(self):
        return f"Optimizing: {self.fitness_function.__name__}, generations: {self.epochs_num}, " \
               f"population size: {self.population_size}, " \
               f"selection method: {self.selection_type.__name__} : {self.selection_args[0]}, " \
               f"crossing method: {self.crossover_type.__name__} : {round(self.crossover_prob, 2)} , " \
               f"inversion probability: {round(self.inversion_prob, 2)}," \
               f" number of selecting elites: {self.elite_strategy_num}," \
               f" evolution time: {round(self.time, 2)}s, " \
               f"best individual found in {self.best_individual_generation}th generation " \
               f"with value {self.best_individual.evaluate(self.fitness_function)} " \
               f"in point {self.best_individual.get_decimal_value_of_chromosomes()}"
