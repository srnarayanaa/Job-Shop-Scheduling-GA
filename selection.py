import random
import numpy as np 
import pandas as pd 
import time

def weightRandom(chromosomes):
    maxVal = sum(fitness(chromosome) for chromosome in chromosomes)
    choice = random.uniform(0, max)
    curr = 0

    for chromosome in chromosomes:
        curr += fitness(chromosome)
        if curr > choice:
            return chromosome

def selection(chromosomes, population_size):
	selectedChromosomes = list()
	for i in range(population_size):
		selectedChromosomes.append(weightRandom(chromosomes))

	return selectedChromosomes
