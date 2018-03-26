# Putting it All Together

Believe it or not, we've implemented everything we need for a genetic algorithm! Now we need to be able to run it.

Let's define a few auxiliary functions that will be helpful for displaying our algorithm running.

<hr />

##### ```get_best()```
When displaying the results, we don't really want to show every member of the population, just the best! So let's make a function in the ```Population``` class that will get the best member of the population.

```python
def get_best(self):
  best = self.population[0]
  for organism in self.population:
    if organism.fitness >= best.fitness:
      best = organism
  return best
```

##### The main loop

Let's now define how we're going to run this!

What we need to do:
1. Define the Hyperparameters
2. Initialize the Population
3. Run ```natural_selection()``` until the best organism in the population has optimal fitness.
  * Note that a lot of times with genetic algorithms, you won't know what the optimal fitness is, so you would just run the algorithm for a large number of generations. In our case, we know the optimal fitness will be 1.0, because that corresponds to all the characters matching.

Create a new file **in the same directory as genetic.py** called ```main.py```, and make it look like this:

```python
from genetic import Population

population_size = 100
mutation_rate = 0.01
target_word = "The greatest enemy of knowledge is not ignorance, it is the illusion of knowledge."

p = Population(population_size, mutation_rate, target_word)
while p.get_best().fitness < 1.0:
  print(''.join(p.get_best().genotype))
  p.natural_selection()
print(''.join(p.get_best().genotype))
```

Run it and see what happens! If all went well, you should see the string start to look like the quote. Congratulations! You've successfully implemented a genetic algorithm!

[Part 6: Where to go from here]()
