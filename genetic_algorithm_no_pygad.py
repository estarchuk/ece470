import os
import pygad
import numpy
import pandas as pd
import random
from datetime import datetime
# tuples containing the types and dopants for the mushroom
cultmed = ("PDA","SPDA","YDA","MEA")
nitri_source = ("NH4CL","N2H8SO4","Nh2CONH2","1% peptone","1% malt extract","1% soybean powder","1% yeast extract")
carb_source = ("glucose","dextrose","fructose","maltose","sucrose","molasses")
substrates = ("sugarcane residue","coconut shell fibre","corn cob","corn straw","acacia sawdust","wild grass","mixed sawddust","cow manure")
# geneset class type for mushroom condition
first_sample = True
old_gen = []
gene_sets = []
curr_size = []
fitness = []
growth = []
num_samples = 4
crossover_mutation_test_genes = []
length  = 13

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

def print_gene_sets():
    global gene_sets
    tally = 1
    for gs in gene_sets:
        print(f"No:{tally}\nGeneset:\nSubstrate Type:{gs.substrate_type}\nNitrogenDoping:{gs.nitrogen_doping}\nNitrogen Source:{gs.nitrogen_source}\nCarbon Source:{gs.carbon_source}\nCarbon Doping:{gs.carbon_doping}\nTemp Min:{gs.temp_min}\nTemp Max:{gs.temp_max}\nCulture Media:{gs.culture_media}\nHumidity Min:{gs.humidity_min}\nHumidity Max:{gs.humidity_max}\nDaylight Ratio:{gs.daylight_ratio}\nLight Intensity:{gs.light_intensity}\nLight Color Temp:{gs.light_color_temp}\n")
        tally += 1
    return

def print_old_gen():
    global old_gen
    tally = 1
    for gs in old_gen:
        print(f"No:{tally}\nGeneset:\nSubstrate Type:{gs.substrate_type}\nNitrogenDoping:{gs.nitrogen_doping}\nNitrogen Source:{gs.nitrogen_source}\nCarbon Source:{gs.carbon_source}\nCarbon Doping:{gs.carbon_doping}\nTemp Min:{gs.temp_min}\nTemp Max:{gs.temp_max}\nCulture Media:{gs.culture_media}\nHumidity Min:{gs.humidity_min}\nHumidity Max:{gs.humidity_max}\nDaylight Ratio:{gs.daylight_ratio}\nLight Intensity:{gs.light_intensity}\nLight Color Temp:{gs.light_color_temp}\n")
        tally += 1
    return

def save_to_file():
    now = datetime.now().strftime('%y-%m-%d-%H%M%S')
    name = "ga_instance" + now + ".txt"
    f = open(name, 'w')
    for gs in gene_sets:
        f.write(f"Substrate Type:{gs.substrate_type}\nNitrogenDoping:{gs.nitrogen_doping}\nNitrogen Source:{gs.nitrogen_source}\nCarbon Source:{gs.carbon_source}\nCarbon Doping:{gs.carbon_doping}\nTemp Min:{gs.temp_min}\nTemp Max:{gs.temp_max}\nCulture Media:{gs.culture_media}\nHumidity Min:{gs.humidity_min}\nHumidity Max:{gs.humidity_max}\nDaylight Ratio:{gs.daylight_ratio}\nLight Intensity:{gs.light_intensity}\nLight Color Temp:{gs.light_color_temp}\n\n")
    f.close()

def read_from_file():
    files = os.listdir(os.curdir)
    files = filter(os.path.isfile, os.listdir( os.curdir ) )
    global old_gen
    l = []
    for f in files:
        if f.endswith('.txt'):
            l.append(f)
    l.sort(reverse=True)
    print("File opened!\n")
    f = open(l[0], 'r')
    for i in range(num_samples):
        temp_substrate = f.readline().split(':')[1].rstrip()
        temp_nitri_dope = f.readline().split(':')[1].rstrip()
        temp_nitri_sour = f.readline().split(':')[1].rstrip()
        temp_carb_sour = f.readline().split(':')[1].rstrip()
        temp_carb_dop = f.readline().split(':')[1].rstrip()
        temp_temp_min = f.readline().split(':')[1].rstrip()
        temp_temp_max = f.readline().split(':')[1].rstrip()
        temp_culmedia = f.readline().split(':')[1].rstrip()
        temp_humi_min = f.readline().split(':')[1].rstrip()
        temp_humi_max = f.readline().split(':')[1].rstrip()
        temp_day_ratio = f.readline().split(':')[1].rstrip()
        temp_light_inten = f.readline().split(':')[1].rstrip()
        temp_light_color = f.readline().split(':')[1].rstrip()
        old_gen.append(gene_set(temp_substrate,temp_nitri_dope,temp_nitri_sour,temp_carb_sour,temp_carb_dop,temp_temp_min,temp_temp_max,temp_culmedia,temp_humi_min,temp_humi_max,temp_day_ratio,temp_light_inten,temp_light_color))
        f.readline()
    f.close()
    

def initial_gene():
    global gene_sets
    for i in range(num_samples):
        temp_substrate = random.choice(substrates)
        temp_nitri_dope = random.uniform(1.0,2.0)
        temp_nitri_sour = random.choice(nitri_source)
        temp_carb_sour = random.choice(carb_source)
        temp_carb_dop = random.uniform(40,60)
        temp_temp_min = random.uniform(15,20)
        temp_temp_max = random.uniform(20,25)
        temp_culmedia = random.choice(cultmed)
        temp_humi_min = random.randint(85,90)
        temp_humi_max = random.randint(90,95)
        temp_day_ratio = random.uniform(33,50)
        temp_light_inten = random.randint(500,1000)
        temp_light_color = random.randint(5000,6500)
        gene_sets.append(gene_set(temp_substrate,temp_nitri_dope,temp_nitri_sour,temp_carb_sour,temp_carb_dop,temp_temp_min,temp_temp_max,temp_culmedia,temp_humi_min,temp_humi_max,temp_day_ratio,temp_light_inten,temp_light_color))

# Crossover function, picks a semi-random amount of genes per parent to give to offspring
def crossover(parent1, parent2):
    random.seed()
    split = random.randrange(1, 12)
    substrate = parent1.substrate_type
    if split > 1:
        nd = parent1.nitrogen_doping
    else:
        nd = parent2.nitrogen_doping
    
    if split > 2:
        ns = parent1.nitrogen_source
    else:
        ns = parent2.nitrogen_source

    if split > 3:
        cs = parent1.carbon_source
    else:
        cs = parent2.carbon_source

    if split > 4:
        cd = parent1.carbon_doping
    else:
        cd = parent2.carbon_doping

    if split > 5:
        t_min = parent1.temp_min
    else:
        t_min = parent2.temp_min

    if split > 6:
        t_max = parent1.temp_max
    else:
        t_max = parent2.temp_max

    if split > 7:
        cm = parent1.culture_media
    else:
        cm = parent2.culture_media

    if split > 8:
        h_min = parent1.humidity_min
    else:
        h_min = parent2.humidity_min

    if split > 9:
        h_max = parent1.humidity_max
    else:
        h_max = parent2.humidity_max

    if split > 10:
        dr = parent1.daylight_ratio
    else:
        dr = parent2.daylight_ratio

    if split > 11:
        li = parent1.light_intensity
    else:
        li = parent2.light_intensity
    
    lc = parent2.light_color_temp
    gene_sets.append(gene_set(substrate, nd, ns, cs, cd, t_min, t_max, cm, h_min, h_max, dr, li, lc))

# Mutation function, picks a random gene(s) from a given set to mutate
def mutation():
    global gene_sets
    random.seed()
    for i in range(num_samples):
        chance = random.randrange(0,100)
        if(chance <= 10):
            num_mutation_alleles = random.randrange(0, 5)
            for i in range(num_mutation_alleles):
                al = random.randrange(0, 13)
                if al == 0:
                    temp_substrate = random.choice(substrates)
                    gene_sets[i].substrate_type = temp_substrate
                elif al == 1:
                    temp_nitri_dope = random.uniform(1.0,2.0)
                    gene_sets[i].nitrogen_doping = temp_nitri_dope
                elif al == 2:
                    temp_nitri_sour = random.choice(nitri_source)
                    gene_sets[i].nitrogen_source = temp_nitri_sour
                elif al == 3:
                    temp_carb_sour = random.choice(carb_source)
                    gene_sets[i].carbon_source = temp_carb_sour
                elif al == 4:
                    temp_carb_dop = random.uniform(40,60)
                    gene_sets[i].carbon_doping = temp_carb_dop
                elif al == 5:
                    temp_temp_min = random.uniform(15,20)
                    gene_sets[i].temp_min = temp_temp_min
                elif al == 6:
                    temp_temp_max = random.uniform(20,25)
                    gene_sets[i].temp_max = temp_temp_max
                elif al == 7:
                    temp_culmedia = random.choice(cultmed)
                    gene_sets[i].culture_media = temp_culmedia  
                elif al == 8:
                    temp_humi_min = random.randint(85,90)
                    gene_sets[i].humidity_min = temp_humi_min
                elif al == 9:
                    temp_humi_max = random.randint(90,95)
                    gene_sets[i].humidity_max = temp_humi_max
                elif al == 10:
                    temp_day_ratio = random.uniform(33,50)
                    gene_sets[i].daylight_ratio = temp_day_ratio
                elif al == 11:
                    temp_light_inten = random.randint(500,1000)
                    gene_sets[i].light_intensity = temp_light_inten
                elif al == 12:
                    temp_light_color = random.randint(5000,6500)
                    gene_sets[i].light_color_temp = temp_light_color

def main():
    if first_sample == True:
        initial_gene()
        print_gene_sets()
        save_to_file()
        exit()
    else:
        read_from_file()
        print_old_gen()
        global growth
        global curr_size
        global fitness
        #Currently asks for growth rate but could be edited to save curr_size in file to calculate growth rate
        for i in range(num_samples):
            curr_size.append(input(f"Enter the Current Size of Sample {i+1}:\n"))
            growth.append(input(f"Enter the Growth Rate of Sample {i+1}:\n"))
            fitness.append(curr_size[i] + growth[i])

        #Currently crossing over 1-2, 1-3, 1-4, 2-3
        crossover(old_gen[0], old_gen[1])
        crossover(old_gen[0], old_gen[2])
        crossover(old_gen[0], old_gen[3])
        crossover(old_gen[1], old_gen[2])
        mutation()
        print_gene_sets()
        save_to_file()
        exit()


if __name__ == "__main__":
    main()
