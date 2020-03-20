import numpy as np
import bitstring


def calculate_chain_length(range_start, range_end, acc):
    # range_start = a, range_end = b, acc = liczba cyfr znaczących w wyniku
    if range_start > range_end:
        print("Wrong range")
    else:
        return np.math.ceil(np.math.log2(abs(range_end - range_start) * pow(10, acc)))


def generate_individual(bits_in_array):
    return np.random.randint(0, 2, size=bits_in_array)


def generate_population(population_size):
    pop = []
    for i in population_size:
        pop.append(generate_individual)


a = -10
b = 10
accuracy = 6

chain_length = calculate_chain_length(a, b, accuracy)
individual = generate_individual(chain_length)
print(individual)
