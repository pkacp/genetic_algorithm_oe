import numpy as np

from src.BinaryChromosome import BinaryChromosome
from src.Population import Population


class Evolution:
    def __init__(self, epochs_num, population_size, range_start, range_end, accuracy, fitness_function, searching_value,
                 chromosome_type, chromosomes_number, selection_type, selection_args, crossover_type, crossover_prob,
                 mutation_type, mutation_prob, elite_strategy_num=0):
        self.epochs_num = epochs_num
        self.population_size = population_size
        self.population_set = set()
        self.elite_strategy_num = elite_strategy_num
        self.best_individuals = set()
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
        self.number_of_genes = BinaryChromosome.calculate_chain_length(range_start, range_end, accuracy)

    def run(self):
        next_generation_individuals = np.array([])
        for generation in range(self.epochs_num):
            new_population = Population(self.chromosome_type, self.population_size, self.chromosomes_number,
                                        self.number_of_genes, self.range_start, self.range_end, self.fitness_function,
                                        self.searching_value, self.elite_strategy_num, next_generation_individuals)
            self.population_set.add(new_population)
            new_population.elite_strategy()
            self.best_individuals.add(new_population.best_individuals)
            print("elites")
            print(self.best_individuals)
            num_individuals_to_select = self.population_size - len(self.best_individuals)
            print(num_individuals_to_select)
            selected_individuals = new_population.selection(self.selection_type, num_individuals_to_select,
                                                            self.searching_value, [])
            print("selected_individuals")
            print(selected_individuals)
            # individuals_for_crossing
            print(generation)
