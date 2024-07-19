import os
import pygad
import numpy
import pandas as pd
import random
from datetime import datetime
# tuples containing the types and dopants for the mushroom
substrates = ("PDA","SPDA","YDA","MEA")
nitri_source = ("Coffee Grounds","NH4CL","N2H8SO4","Nh2CONH2","1% peptone","1% malt extract","1% soybean powder","1% yeast extract")
carb_source = ("glucose","dextrose","fructose","maltose","sucrose","molasses")
cultmed = ("sugarcane residue","coconut shell fibre","corn cob","corn straw","acacia sawdust","wild grass","mixed sawddust","cow manure")
# geneset class type for mushroom condition
class gene_set:
    def __init__(the_gene_set, substrate_type, nitrogen_doping, nitrogen_source, carbon_source, carbon_doping, temp_min, temp_max, culture_media, humidity_min, humidity_max, daylight_ratio, light_intensity, light_color_temp):
        the_gene_set.substrate_type : str = substrate_type
        the_gene_set.nitrogen_doping : float = nitrogen_doping
        the_gene_set.nitrogen_source : str = nitrogen_source
        the_gene_set.carbon_source : str = carbon_source
        the_gene_set.carbon_doping : float = carbon_doping
        the_gene_set.temp_min : float = temp_min
        the_gene_set.temp_max : float = temp_max
        the_gene_set.culture_media : str = culture_media
        the_gene_set.humidity_min : int = humidity_min
        the_gene_set.humidity_max : int = humidity_max
        the_gene_set.daylight_ratio : float = daylight_ratio
        the_gene_set.light_intensity : int = light_intensity
        the_gene_set.light_color_temp : int = light_color_temp

def initial_gene():
    gene_sets = []
    for i in range(4):
        temp_substrate = substrates(random.randint(0,3))
        temp_nitri_dope = random.uniform(1.0,2.0)
        temp_nitri_sour = nitri_source(random.randint(0,8))
        temp_carb_sour = carb_source(random.randint(0,5))
        temp_carb_dop = random.uniform(40,60)
        temp_temp_min = random.uniform(15,20)
        temp_temp_max = random.uniform(20,25)
        temp_culmedia = cultmed(random.randint(0,7))
        temp_humi_min = random.randint(85,90)
        temp_humi_max = random.randint(90,95)
        temp_day_ratio = random.uniform(33,50)
        temp_light_inten = random.randint(500,1000)
        temp_light_color = random.randint(5000,6500)
        gene_sets.append(gene_set(temp_substrate,temp_nitri_dope,temp_nitri_sour,temp_carb_sour,temp_carb_dop,temp_temp_min,temp_temp_max,temp_culmedia,temp_humi_min,temp_humi_max,temp_day_ratio,temp_light_inten,temp_light_color))


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