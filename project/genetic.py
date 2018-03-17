class Organism:
    def __init__(self, genes): # Constructor method
        # The genotype, just a list of characters
        self.genotype = genes

        # The phenotype, just the genotype converted to a string
        self.phenotype = ''.join(self.genotype)

    def calc_fitness(self, target):
        correct_cnt = 0
        for gene, actual in zip(self.genotype, target):
            if gene == actual:
                correct_cnt += 1
        return correct_cnt/len(target)
