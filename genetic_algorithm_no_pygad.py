import os
import pygad
import numpy
import pandas as pd
import random
from datetime import datetime

function_inputs = [[1,2,3,4,5,6,7,8,9], [2,3,4,5,1,25,36,78,98], [3,4,5,1,2], [4,5,1,2,3]]
random_test = []
length  = 9

def crossover(function_input1, function_input2):
    global random_test
    random.seed()
    x_alleles  = random.randrange(1,length)
    y_alleles = length - x_alleles
    for i in range(x_alleles):
        random_test.append(function_input1[i])
    for i in range(y_alleles):
        random_test.append(function_input2[x_alleles + i])

def mutation():
    global random_test
    random.seed()
    chance = random.randrange(0,100)
    mutation_alleles = []
    if(chance <= 10):
        # Depending on the allele selected we'll need acceptable ranges
        mutation_amount = random.randrange(1,3)
        for i in range(mutation_amount):
            mutation_alleles.append(random.randrange(0, len(random_test)))
        for alleles in mutation_alleles:
            random_test[alleles] += 100000

def main():
    crossover(function_inputs[0], function_inputs[1])
    mutation()
    print(random_test)


if __name__ == "__main__":
    main()