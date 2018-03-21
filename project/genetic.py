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
        return correct_cnt/len(target)

class Population:
    def __init__(self, pop_size, ):
