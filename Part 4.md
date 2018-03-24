# Natural Selection

Now that we have a population of organisms that all have a fitness associated with them, we can perform **Natural Selection** in order to have that population pass it's very best genes onto the next generation! (_And all immediately die..._)

Recall how we defined natural selection in part 2:
> * A **mating pool** is established, where the organisms in the population with the highest fitness will be more likely to be selected from the mating pool.
> * Two organisms are randomly selected from the mating pool, and they will pass their genes on to a new organism via the **crossover** function. This new organism is then **mutated** and added to the new population. This is repeated until the new population is full. (Note that the old population just dies out)

Let's work backwards and make that second paragraph more concrete. Specifically, we need to define a way for two organisms to generate offspring (i.e., a **crossover function**); and, a way to **mutate** an organism. Let's start with the **crossover function**.

Let's think about how this might work. Keep the task of the crossover function in mind

> We have **2 genotypes**, we want to mix the two together to make one genotype.

Our genotypes are just lists. We basically want a new list where 50% of the elements are from the first list and 50% are from the second. There are several ways of doing this, but we'll go with the easy route of just splitting down the middle.

Add this function to the ```Organism``` class.
```python
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
```

<hr />

#### Mutation

Now for mutation, we basically want to randomly change a gene in the sequence. Add this function into the ```Organism``` class, we'll examine it later.

```python
def mutate(self, mutation_rate):
  for i in range(len(self.genotype)):
    if random.random() <= mutation_rate:
      self.genotype[i] = random.choice(self.nucleotides)
```

So what's going on here? Well, we loop through all the genes in the genotype. We then generate a random number between 0 and 1 via ```random.random()```. If that number is < mutation_rate, we replace that gene in the genotype with a new random gene.

To get an idea of how this works, imagine that we set ```mutation_rate = 0.1```. Since ```random.random()``` generates a random number between 0 and 1, ```random.random()``` will output a number that is <= 0.1 approximately 10% of the time. It follows then that ~10% of the genes in the genotype will be replaced by new, random genes.

<hr />

#### Creating the Mating Pool

Now we need to create a **mating pool**, what exactly is that though? Let's look at what function a mating pool serves:

The basic idea of natural selection is that organisms who are more _fit_ are more likely to reproduce, and therefore pass their genes onto the next generation. Let's formalize this a bit more:

> When reproduction happens, two organisms in the population are selected to reproduce, and, their child is added to the new population. This is repeated until the new population is big enough to replace the old population.
> The selection of the two organisms is done in a matter so that organisms with higher fitness are more likely to be selected.

So we need some kind of mechanism for performing this selection. A naive way is to actually create a **mating_pool** list where the number of times an organism is present in that list is proportional to their fitness. While this would work, it is memory intensive and there's a better solution.

##### Our selection method
Warning: Math Ahead.

Suppose there's some organism _i_ with fitness _f<sub>i</sub>_. Then the probability _p<sub>i</sub>_ that _i_ will be selected to reproduce is given by:
![Equation, Credit to Wikipedia](https://wikimedia.org/api/rest_v1/media/math/render/svg/4890d45d9732279faf49a9892f9f5f200b7043d2)

<hr />

Let's implement this! I'm going to be using a tool called ```numpy``` to do this, as it has a function that makes this super easy. But first you need to install it!
```bash
pip install numpy
```
You may need to do ```pip3``` instead of ```pip```.

And make sure to add this line at the beginning of your program:
```python
import numpy as np
```

Awesome, let's make a static ```select_two_organisms``` function as part of the ```Population``` class.
```python
def select_two_organisms(self):
  fitnesses = np.array([o.fitness for o in self.population])
  fit_sum = fitnesses.sum()
  p = list(map(lambda x: x/fit_sum, fitnesses))
  mates = np.random.choice(self.population, size=2, p=p)
  return (mates[0], mates[1])
```
If you don't understand all this that's fine. Just know that we're following the selection algorithm from earlier, and that it will return two organisms who were selected in a way that prioritized their fitnesses.

<hr />

##### The ```natural_selection``` function

Recall the natural selection algorithm we defined earlier:

> * A **mating pool** is established, where the organisms in the population with the highest fitness will be more likely to be selected from the mating pool.
> * Two organisms are randomly selected from the mating pool, and they will pass their genes on to a new organism via the **crossover** function. This new organism is then **mutated** and added to the new population. This is repeated until the new population is full. (Note that the old population just dies out)

We now have everything we need to implement this!

Add this function to the ```Population``` class:
```python
def natural_selection(self):
  new_pop = []
  for i in range(self.pop_size):
    a, b = self.select_two_organisms()
    new_organism = a.crossover(b)
    new_organism.mutate(self.mutation_rate)
    new_pop.append(new_organism)
  self.population = new_pop
  self.calc_fitness()
```

[Part 5: Putting it all Together]()
