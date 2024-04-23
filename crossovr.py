import random


def binary_crossover(parent1, parent2):
    """
    Perform crossover operation on two binary strings (chromosomes).

    Args:
    - parent1 (str): The first parent chromosome.
    - parent2 (str): The second parent chromosome.

    Returns:
    - child1 (str): The first child chromosome after crossover.
    - child2 (str): The second child chromosome after crossover.
    """
    # Randomly choose a crossover point
    crossover_point = random.randint(1, len(parent1) - 1)

    # Perform crossover
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2


# Example usage
population = ['110010', '101101', '011011', '111000', '010101', '100110']

# Perform crossover for a certain percentage of the population
crossover_rate = 0.25
num_pairs = len(population) // 2

# Randomly choose pairs of parents for crossover
pairs = random.sample(population, k=num_pairs * 2)

# Perform crossover for each pair of parents
for i in range(0, len(pairs), 2):
    parent1, parent2 = pairs[i], pairs[i + 1]
    if random.random() < crossover_rate:
        child1, child2 = binary_crossover(parent1, parent2)
        print(f"Parent 1: {parent1}, Parent 2: {parent2}, Child 1: {child1}, Child 2: {child2}")
    else:
        print(f"No crossover for Parent 1: {parent1}, Parent 2: {parent2}")
