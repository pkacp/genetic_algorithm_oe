import matplotlib.pyplot as plt
import numpy as np
import csv
import time


class DataAnalyzer:
    def __init__(self, evolution, do_best_val, do_mean, do_std):
        self.evolution = evolution
        self.do_best_val = do_best_val
        self.do_mean = do_mean
        self.do_std = do_std
        print("Some plotting")
        self.plotting_and_saving_to_csv()

    def plotting_and_saving_to_csv(self):
        with open('../csv/datafile.csv', mode='w') as employee_file:
            evolution_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            evolution_writer.writerow(['Generarion num', 'Best', 'Mean', 'Standard Deviation'])
            generation = 1
            values = []
            for population in self.evolution.population_set:
                evaluated_values = population.evaluated_starting_individuals[:, 1]
                best_in_pop = population.searching_value(evaluated_values)
                mean_in_pop = np.mean(evaluated_values)
                sd_in_pop = np.std(evaluated_values)
                values_in_pop = [generation, best_in_pop, mean_in_pop, sd_in_pop]
                values.append(values_in_pop)
                evolution_writer.writerow(values_in_pop)
                generation = generation + 1
        values = np.asarray(values)
        # timestamp = int(time.time())
        timestamp = 0
        if self.do_best_val:
            plt.plot(values[:, 1], color='green')
            plt.title('Function best value in iteration')
            plt.xlabel('Generation')
            plt.ylabel('Best value')
            plt.savefig(f'../plots/function_value_in_iteration_{timestamp}.png')
            plt.cla()
        if self.do_mean:
            plt.plot(values[:, 2], color='red')
            plt.title('Function mean value in iteration')
            plt.xlabel('Generation')
            plt.ylabel('Mean value')
            plt.savefig(f'../plots/mean_function_value_in_iteration_{timestamp}.png')
            plt.cla()
        if self.do_std:
            plt.plot(values[:, 3], color='blue')
            plt.title('Function standard deviation in iteration')
            plt.xlabel('Generation')
            plt.ylabel('Best value')
            plt.savefig(f'../plots/sd_in_iteration_{timestamp}.png')
            plt.cla()
