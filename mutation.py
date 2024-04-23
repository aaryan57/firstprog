import random


def binary_mutation(chromosome, mutation_rate):
    """
    Perform mutation operation on a binary string (chromosome).

    Args:
    - chromosome (str): The chromosome to be mutated.
    - mutation_rate (float): The probability of mutation for each bit.

    Returns:
    - mutated_chromosome (str): The mutated chromosome.
    """
    mutated_chromosome = ""
    for bit in chromosome:
        if random.random() < mutation_rate:
            # Flip the bit (mutate)
            mutated_chromosome += '0' if bit == '1' else '1'
        else:
            mutated_chromosome += bit
    return mutated_chromosome


# Example usage
population = ['110010', '101101', '011011', '111000', '010101', '100110']

# Mutation rate
mutation_rate = 0.1

# Perform mutation for each chromosome in the population
mutated_population = []
for chromosome in population:
    mutated_chromosome = binary_mutation(chromosome, mutation_rate)
    mutated_population.append(mutated_chromosome)

# Output
for i, (original, mutated) in enumerate(zip(population, mutated_population)):
    print(f"Original chromosome {i + 1}: {original}, Mutated chromosome {i + 1}: {mutated}")
