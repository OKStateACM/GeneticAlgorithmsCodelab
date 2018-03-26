from genetic import Population
import sys

target_word, mutation_rate, pop_size = sys.argv[1], sys.argv[2], sys.argv[3]

p = Population(pop_size, mutation_rate, target_word)
while p.get_best().fitness < 1.0:
    print(''.join(p.get_best().genotype) + '|' + p.get_best().fitness())
print(''.join(p.get_best().genotype) + '|' + p.get_best().fitness())
