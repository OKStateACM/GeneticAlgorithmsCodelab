import numpy as np
import string
import random

class Organism:
    def __init__(self, gene_length): # Constructor method
        # The "Nucleotides", i.e. what each gene is made of
        self.nucleotides = list(string.ascii_letters + '.,!?, ')

        # The genotype, just a list of characters
        self.genotype = []
        for i in range(gene_length):
          self.genotype.append(random.choice(self.nucleotides))

        # The phenotype, just the genotype converted to a string
        self.phenotype = ''.join(self.genotype)

    def calc_fitness(self, target):
        correct_cnt = 0
        for gene, actual in zip(self.genotype, target):
            if gene == actual:
                correct_cnt += 1
        self.fitness = (correct_cnt/len(target)) ** 100

    def crossover(self, partner):
        child_genome = []

        for i in range(len(self.genotype)):
            if (i < len(self.genotype)/2):
                child_genome.append(self.genotype[i])
            else:
                child_genome.append(partner.genotype[i])

        child = Organism(len(self.genotype))
        child.genotype = child_genome;

        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genotype)):
            if random.random() <= mutation_rate:
                self.genotype[i] = random.choice(self.nucleotides)

class Population:
    def __init__(self, pop_size, mutation_rate, target_word):
        self.target = target_word
        self.mutation_rate = mutation_rate
        self.pop_size = pop_size

        self.population = []
        for i in range(pop_size):
            self.population.append(Organism(len(self.target)))

        self.calc_fitness()

    def calc_fitness(self):
        for organism in self.population:
            organism.calc_fitness(self.target)

    def select_two_organisms(self, p):
        mates = np.random.choice(self.population, size=2, p=p)
        return (mates[0], mates[1])

    def natural_selection(self):
        new_pop = []
        fitnesses = np.array([o.fitness for o in self.population])
        fit_sum = fitnesses.sum()
        p = list(map(lambda x: x/fit_sum, fitnesses))
        for i in range(self.pop_size):
            a, b = self.select_two_organisms(p)
            new_organism = a.crossover(b)
            new_organism.mutate(self.mutation_rate)
            new_pop.append(new_organism)
        self.population = new_pop
        self.calc_fitness()

    def get_best(self):
        best = self.population[0]
        for organism in self.population:
            if organism.fitness >= best.fitness:
                best = organism
        return best
