# How this is going to work

Genetic algorithms can be confusing at first, so let's outline what all will happen in order to solve the problem presented earlier.

1. A **population** of **organisms** will be created.
  * Each **organism** will have a **genotype** (DNA) and a **phenotype**. The **genotype** is the organisms genes. The **phenotype** is the expression of those genes.
2. For each **organism** in the **population**, their **fitness** will be calculated using a **fitness function**.
3. **Natural Selection** will occur:
  * A **mating pool** is established, where the organisms in the population with the highest fitness will be more likely to be selected from the mating pool.
  * Two organisms are randomly selected from the mating pool, and they will pass their genes on to a new organism via the **crossover** function. This new organism is then **mutated** and added to the new population. This is repeated until the new population is full. (Note that the old population just dies out)
4. Go back to step 2. Repeat

Note that this is just one approach to genetic algorithms, and the exact algorithm you use will be completely dependent on the problem you are solving.

![Genetic Algorithm Animation](https://www.ewh.ieee.org/soc/es/May2001/14/GAPROC0.GIF)

<hr />

Let's think now about how this applies to our problem. For any genetic algorithm, a lot of things are going to be same. But you **always** need to define two things:
  1. What the genotype and phenotype of the organism will be.
  2. The fitness function

### Organisms
As stated above, organisms have **genotypes** and **phenotypes**. For this project, the genotype and phenotype will actually be the same. We're going to make the genes of each organism be the characters that it produces.

For example, the **genotype** of an organism might be:
```python
"go pokes"
```
It's **phenotype** would then be:
```python
"go pokes"
```

In fact, let's go ahead and make an ```Organsim``` class in python. Make a new python file (call it whatever you want)

```python
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
```

All this is doing is defining a class called Organism. In the constructor we pass in an integer called ```gene_length```. This is just how long the gene sequence should be. We then create the **genotype** by appending a random character ```gene_length``` times. The phenotype is then just the genotype converted to a string.

### Fitness function
The **fitness function** is one of the most important parts of any genetic algorithm. You can think of it as a function that _tells you how good an organism is_, and therefore how likely it should be to transfer it's genes to the next generation. (Think _survival of the fittest_)

The fitness function for our project is going to be relatively simple. Since we know the correct answer, we can just see how many characters are in the right place. Let's write it! In the Organism class, define a new function called ```calc_fitness```

```python
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
        self.fitness = correct_cnt/len(target)
```

#### Notes for those maybe less familiar with python:
The only kind of confusing thing here is the line
is:
```python
for gene, actual in zip(self.genotype, target):
```

This is just how for loops are done in python. If we were just looping through a list called ```l```, we could print out every element of the list by doing something like:

```python
for item in l:
  print(item)
```

The ```zip``` function just combines the two lists so that you can loop through them both at the same time. For example, if we had two lists ```l``` and ```w```, and we wanted to print each element of l and w on a new line, we could do something like this:

```python
for l_item, w_item in zip(w, l):
  print(l_item, ', ', w_item)
```

[Part 3: Building up the Population class]()
