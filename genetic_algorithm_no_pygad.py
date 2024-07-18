import os
import pygad
import numpy
import pandas as pd
import random
from datetime import datetime

gene_sets = [[1,2,3,4,5,6,7,8,9], [2,3,4,5,1,25,36,78,98], [3,4,5,1,2,56,84,12,35], [4,5,1,2,3,21,35,83,67]]
crossover_mutation_test_genes = []
length  = 9

# Crossover function, picks a semi-random amount of genes per parent to give to offspring
def crossover(parent1, parent2):
    global crossover_mutation_test_genes
    random.seed()
    x_alleles  = random.randrange(1,length)
    y_alleles = length - x_alleles
    for i in range(x_alleles):
        crossover_mutation_test_genes.append(parent1[i])
    for i in range(y_alleles):
        crossover_mutation_test_genes.append(parent2[x_alleles + i])

# Mutation function, picks a random gene(s) from a given set to mutate
def mutation():
    global crossover_mutation_test_genes
    random.seed()
    chance = random.randrange(0,100)
    mutation_alleles = []
    if(chance <= 10):
        # Depending on the gene(s) selected we'll need acceptable ranges, 0-100 for now
        mutation_amount = random.randrange(1,3)
        for i in range(mutation_amount):
            mutation_alleles.append(random.randrange(0, len(crossover_mutation_test_genes)))
        for alleles in mutation_alleles:
            crossover_mutation_test_genes[alleles] += random.randrange(1,101)

def main():
    crossover(gene_sets[0], gene_sets[1])
    mutation()
    print(crossover_mutation_test_genes)


if __name__ == "__main__":
    main()