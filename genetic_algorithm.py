import os
import pygad
import numpy
import pandas as pd
from datetime import datetime

#Need to change
num_samples = 8

#NEED TO DO
function_inputs = [4,-2,3.5,5,-11,-4.7]
desired_output = 44

def get_measurements():
    sample_measurements = []
    for i in range(num_samples):
        curr_size = input("Please enter current size for sample " + str(i) +":\n")
        growth_rate = input("Please enter growth rate for sample " + str(i) +":\n")
        sample_measurements.append([curr_size, growth_rate])
    return sample_measurements

def fitness_func(ga_instance, solution, solution_idx):
    global measurements
    fitness = measurements[solution_idx][0] + measurements[solution_idx][1]
    return fitness

def main():
    files = os.listdir(os.curdir)
    files = filter(os.path.isfile, os.listdir( os.curdir ) )
    l = []
    for f in files:
        if f.endswith('.pkl'):
            l.append(f)
    l.sort(reverse=True)

    if not l:
        #NEED TO SET INITIAL SETUP VALUES
        get_measurements()

        function_inputs = [1,3,4,5]

        fitness_function = fitness_func

        num_generations = 50
        num_parents_mating = 4

        sol_per_pop = 8
        num_genes = len(function_inputs)

        init_range_low = -2
        init_range_high = 5

        parent_selection_type = "sss"
        keep_parents = 1

        crossover_type = "single_point"

        mutation_type = "random"
        mutation_percent_genes = 10

        #Also need to add way to use date from big data set if we want that

        ga_instance = pygad.GA(num_generations=num_generations,
                        num_parents_mating=num_parents_mating,
                        fitness_func=fitness_function,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        init_range_low=init_range_low,
                        init_range_high=init_range_high,
                        parent_selection_type=parent_selection_type,
                        keep_parents=keep_parents,
                        crossover_type=crossover_type,
                        mutation_type=mutation_type,
                        mutation_percent_genes=mutation_percent_genes)
    else:
        ga_instance = pygad.load(l[0])

    ga_instance.run()

    #Probably should clean this up
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

    prediction = numpy.sum(numpy.array(function_inputs)*solution)
    print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

    now = datetime.now().strftime('%y-%m-%d-%H%M%S')
    ga_instance.save("ga_instance"+ now)

if __name__ == "__main__":
    main()