from genetic import Population

population_size = 100
mutation_rate = 0.01
target_word = "The greatest enemy of knowledge is not ignorance, it is the illusion of knowledge."

p = Population(population_size, mutation_rate, target_word)
while p.get_best().fitness < 1.0:
    print(''.join(p.get_best().genotype))
    p.natural_selection()
print(''.join(p.get_best().genotype))
