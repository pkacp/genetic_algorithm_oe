import matplotlib.pyplot as plt
import time
from textwrap import wrap
import csv


class DataAnalyzer:
    def __init__(self, evolution, do_best_val, do_mean, do_std):
        self.evolution = evolution
        self.do_best_val = do_best_val
        self.do_mean = do_mean
        self.do_std = do_std
        self.list = []
        print(self.evolution.to_string())

    def plotting_and_saving_to_csv(self):
        timestamp = int(time.time())
        with open(f'../results/datafile_{timestamp}.csv', mode='w') as results_file:
            evolution_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            evolution_writer.writerow(['Generarion num', 'Best', 'Mean', 'Standard Deviation'])
            generation_counter = 0
            for best, mean, std in zip(self.evolution.bests_values, self.evolution.mean_values,
                                       self.evolution.sd_values):
                evolution_writer.writerow([generation_counter, best, mean, std])
                generation_counter = generation_counter + 1
        if self.do_best_val:
            plt.figure(figsize=(12, 9))
            plt.plot(self.evolution.bests_values, color='green')
            plt.title(self.set_title('Function best value in iteration'))
            plt.xlabel('Generation')
            plt.ylabel('Best value')
            plt.savefig(f'../plots/function_value_in_iteration_{timestamp}.png', )
            plt.cla()
            self.list.append("function_value_in_iteration_" + str(timestamp) + ".png")
        if self.do_mean:
            plt.figure(figsize=(12, 9))
            plt.plot(self.evolution.mean_values, color='red')
            plt.title(self.set_title('Function mean value in iteration'))
            plt.xlabel('Generation')
            plt.ylabel('Mean value')
            plt.savefig(f'../plots/mean_function_value_in_iteration_{timestamp}.png')
            plt.cla()
            self.list.append("mean_function_value_in_iteration_" + str(timestamp) + ".png")
        if self.do_std:
            plt.figure(figsize=(12, 9))
            plt.plot(self.evolution.sd_values, color='blue')
            plt.title(self.set_title('Function standard deviation in iteration'))
            plt.xlabel('Generation')
            plt.ylabel('Standard deviation value')
            plt.savefig(f'../plots/sd_in_iteration_{timestamp}.png')
            plt.cla()
            self.list.append("sd_in_iteration_" + str(timestamp) + ".png")

    def get_list(self):
        return self.list

    def set_title(self, current_title):
        return f"{current_title}\n" + "\n".join(wrap(f"{self.evolution.to_string()}", 130))
