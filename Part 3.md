# The Population Class

Recall the algorithm outlined in the beginning of Part 2. We made a basic template for an **organism**; but, those organisms need to exist in a **population** so that **natural selection** can be performed.

So let's make a population class! Add this below your ```Organism``` class definition
```python
class Population:
    def __init__(self, pop_size, mutation_rate, target_word):
        self.target = target_word
        self.mutation_rate = mutation_rate
        self.pop_size = pop_size

        self.population = []
        for i in range(pop_size):
            self.population.append(Organism(len(self.target)))
```

This will provide a basic template for how our population will work. Let's break down the constructor we just wrote:
<br />
1. We are passing in ```pop_size``` (the size of the population), ```mutation_rate``` (we'll talk about this later), and ```target_word``` (the word that we want our algorithm to end up returning)
  * Note that ```target_word``` is something we're including specifically because of the task we're trying to accomplish; whereas, ```pop_size``` and ```mutation_rate``` are something you will have in almost every genetic algorithm.
2. We set instance variables equal to what we passed in.
3. We initialize the population!
  * We're just going to hold each ```Organism``` in a list. The loop generates ```Organisms``` (recall how that is done in the ```Organism``` constructor) and add's them to the list.

Recall the algorithm from [Part 2]():

> 1. A **population** of **organisms** will be created.
> 2. For each **organism** in the **population**, their **fitness** will be calculated using a **fitness function**.
> 3. **Natural Selection** will occur:
> 4. Go back to step 2. Repeat

You've successfully done step 1!
![woohoo](https://media.makeameme.org/created/woohoo-way-to-zczo30.jpg)

Next, we need to do step 2.
> For each **organism** in the **population**, their **fitness** will be calculated using a **fitness function**.

Hopefully these words feel a lot more concrete now.
We've defined each of the bolded words with code!
We have a **population** of **organisms**, and each **organism** has a **fitness** we can calculate using a **fitness function**. Now all we need to do is actually do that for each organism in the population. Pop this method into your **population** class definition:
```python
def calc_fitness(self):
      for organism in self.population:
          organism.calc_fitness(self.target)
```

And let's go ahead and actually call that whenever we initialize the population:
```python
def __init__(self, pop_size, mutation_rate, target_word):
      self.target = target_word
      self.mutation_rate = mutation_rate
      self.pop_size = pop_size

      self.population = []
      for i in range(pop_size):
          self.population.append(Organism(len(self.target)))

      self.calc_fitness()
```

So that takes care of steps 1 and 2 in the algorithm! Now we need to perform **Natural Selection**

[Part 4: Natural Selection](https://github.com/OKStateACM/GeneticAlgorithmsCodelab/blob/master/Part%204.md)
