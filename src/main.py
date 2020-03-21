from src.BinaryChromosome import BinaryChromosome
from src.Population import Population

a = -10
b = 10
accuracy = 6

number_of_genes = BinaryChromosome.calculate_chain_length(a, b, accuracy)

chromosome_size = 1
population_size = 5

pop1 = Population(BinaryChromosome, population_size, chromosome_size, number_of_genes)
pop1.print_population()


epochs_number = 10
