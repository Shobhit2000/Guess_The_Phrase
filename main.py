import random

# the % value of elitism to be performed
ELITISM_FACTOR = 10
MATING_PERCENT = 50
POPULATION_SIZE = 100
TARGET = ""
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ,."_;:!@$[]'''

class Individual(object):
    # A class which represents the outline of an Individual in a generation

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    @classmethod
    def mutated_genes(self):
        # create a completely random chromosome
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(self):
        # create a new chromosome
        global TARGET
        gnome_len = len(TARGET)

        return [self.mutated_genes() for _ in range(gnome_len)] 

    def mate(self, second_parent):
        # create a offspring by using two parent
        child_chromosome = []

        for gp1, gp2 in zip(self.chromosome, second_parent.chromosome):
            prob = random.random()
            if prob <= 0.45:
                child_chromosome.append(gp1)

            elif prob <= 0.9:
                child_chromosome.append(gp2)

            else:
                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)

    def calculate_fitness(self):
        # A method to calculate the fitness of an Individual 
        # Based on the chromosome
        global TARGET
        fitness = 0

        for cg, ct in zip(self.chromosome, TARGET):
            if cg != ct:
                fitness += 1

        return fitness

def main():

    global MATING_PERCENT
    global ELITISM_FACTOR
    global POPULATION_SIZE
    global TARGET

    TARGET = input("Enter the Phrase you want your system to predict: ")
    population = []
    solved = False
    generation = 1

    # create the initial population
    for _ in range(POPULATION_SIZE):
        # generate a new chromosome
        gnome = Individual.create_gnome()

        # generate a new Individual and add it to the population array
        new_Individual = Individual(gnome)
        population.append(new_Individual)
        # print(str(gnome))

    while not solved:
        # sort the population according to the fitness
        # this line sorts Population according to the fitness but since its is popluation.fitness we define it as:
        population = sorted(population, key=lambda x: x.fitness)

        if population[0].fitness <= 0:
            solved = True
            break

        new_population = []

        # perform Elitism
        s = int((ELITISM_FACTOR * POPULATION_SIZE) / 100)
        new_population.extend(population[:s])

        # perform the process of mating
        MATING_FACTOR = 100 - ELITISM_FACTOR
        s = int((MATING_FACTOR * POPULATION_SIZE) / 100)
        # print("hi")
        for _ in range(s):
            real_size = int((MATING_PERCENT * POPULATION_SIZE) / 100)

            # initialize 2 parents
            parent_1 = random.choice(population[:real_size])
            parent_2 = random.choice(population[:real_size])

            child = parent_1.mate(parent_2)
            new_population.append(child)

        population = new_population
        population = sorted(population, key=lambda x: x.fitness)
        print("Generation: {}\t; String: {}\t; Fitness: {}".\
              format(generation,
                     "".join(population[0].chromosome),
                     population[0].fitness))
        generation += 1

    print("Generation: {}\t; String: {}\t; Fitness: {}".\
          format(generation,
                 "".join(population[0].chromosome),
                 population[0].fitness))


if  __name__ == '__main__':
    main()
