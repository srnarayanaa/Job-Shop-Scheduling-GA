import random
import numpy as np 
import pandas as pd 
import time 
from selection import *
from mutation import *
from crossover import *
from fitness import * 
import math
MAX = 10000000000007

def initialise_paramters():
	#size - 25
	#iterations - 1000
	#mutation rate - 2
	#crossover rate - 30
	return [25, 1000, 2, 30]

def populate(size, jobs, operations):
	population = []
	for i in range(size):
		operation_vector, machine_vector = list(), list()

		for job in range(1, jobs+1, 1): operation_vector.extend([job]*operations)
		random.shuffle(operation_vector)

		for machine in range(len(operation_vector)):machine_vector.append(random.randrange(1, machines+1))

		population.append((operation_vector, machine_vector))

	return population	

def checkCross(val):
	return val^1, val == 0

def mutationDriver(post_crossover_vector, population_size, mutation_rate):
	post_mutation_vector = list()
	while index < population_size
		operation_vector, machine_vector = post_crossover_vector[index]
		op, ma = random.randrange(100), random.randrange(100)
	 	if op <mutation_rate:
	 		operation_vector = operationalMutation(operation_vector, machine_vector, random.randrange(len(operation_vector)), len(chromosome_vector[0]))
	 	if ma < mutation_rate:
	 		machine_vector = machineMutation(machine_vector, operation_vector, random.randrange(len(machine_vector)), len(chromosome_vector[0]))
	 	post_mutation_vector.append((operation_vector, machine_vector))

	 return post_mutation_vector

def chooseCross(index1, index2, chromosome_vector, post_selection_vector):
	val1 = chromosome_vector[post_selection_vector[index1]]
	val2 = chromosome_vector[post_selection_vector[index2]]
	return val1[0], val2[0], val1[1], val2[1]

def computation(machines, chromosome_vector, population_size, paramters):
	shortest, fittest_individual = MAX, set()

	for x in range(population_size):
		op, ma = chromosome_vector[x]
		time, dash = fitness(paramters)
		if time < ep_min_time:
			ep_min_time = time 
			fittest_individual = (op, ma)

	op, ma = fittest_individual
	time, reg = fitness(parameters)

	print("Minimal Time : ", time, 'and Sequence is : ')
	for i in range(machines): print(reg[i])
	print()


def main():
	jobs = 4
	machines = 5
	operations = 3
	population_size, iterations, mutation_rate, crossover_rate = initialise_paramters()

	operational_cost = [[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2],
						[6, 7, 2, math.inf, 9, 2]]

	#chromosome_vector = list()
	chromosome_vector = populate()
	fittest_individual, y = set(), 0

	while _ < iterations:
		paramters = [jobs, machines, operations, operation_vector, machine_vector, operational_cost]
		post_selection_vector = selection(chromosome_vector, population_size, paramters)
		post_crossover_vector = list()
		post_mutation_vector = list()
		for x in range(population_size):
			nr = random.randrange(100)
			if nr < crossover_rate:
				crossed, flag = checkCross(crossed)
				if flag:
					opp1, opp2, mp1, mp2 = chooseCross(x, y)

					onew1, onew2, mnew1, mnew2 = operationalCrossover(opp1, opp2), machineCrossover(mp1, mp2)
					pair1, pair2 = (onew1, mnew1), (onew2, mnew2)

					post_crossover_vector.append(pair1)
					post_crossover_vector.append(pair2)
				y = x 

		chromosome_vector = mutationDriver(post_crossover_vector, population_size, mutation_rate)
		paramters = [jobs, machines, operations, operation_vector, machine_vector, operational_cost]
		computation(machines, chromosome_vector, population_size, paramters)
		_ += 1

if __name__ == '__main__':
	main()
