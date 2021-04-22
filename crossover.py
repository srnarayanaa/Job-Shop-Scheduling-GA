import random
import numpy as np 

def verge(chromosome):
	return len(chromosome) // 2 - 1, len(chromosome)

def initialiseChildren(length):
	return [None]*length, [None]*length

def singlePointCrossover(parent1, parent2, x):
	temp1, temp2 = list(), list()
	temp1 = parent1[x:] + parent2[:x]
	temp2 = parent2[x:] + parent1[:x]
	return temp1, temp2

def multiPointCrossover(parent1, parent2, x):
	for i in x:
		temp1, temp2 = singlePointCrossover(parent1, parent2, i)
	return temp1, temp2

def uniformCrossover(parent1, parent2, P):
	for i in range(len(P)):
		if P[i] < 0.5:
			parent1[i], parent2[i] = parent2[i], parent2[i]
	return parent1, parent2

def operationalCrossover(operation_parent1, operation_parent2):
	chromosomeLength, verge = verge(operation_parent1)
	operation_child1, operation_child2 = initialiseChildren(chromosomeLength)

	#One Point Crossover
	operation_child1, operation_child2 = singlePointCrossover(operation_parent1, operation_parent2, verge)

	#Multi Point Crossover
	pointsLength, points = 0, list()
	pointsLength = random.randint(chromosomeLength - 1)

	for x in range(random.randint(pointsLength)):
		X = random.rand(chromosomeLength - 1)
		while X in points:
			X = random.rand(chromosomeLength - 1)
		points.append(X)

	operation_child1, operation_child2 = multiPointCrossover(operation_parent1, operation_parent2, points)

	#Uniform Crossover
	P = np.random.rand(chromosomeLength)
	operation_child1, operation_child2 = uniformCrossover(operation_parent1, operation_parent2, P)

	return operation_child1, operation_child2

def machineCrossover(machine_parent1, machine_parent2):
	chromosomeLength, verge = verge(operation_parent1)
	machine_child1, machine_child2 = initialiseChildren(chromosomeLength)

	#One Point Crossover
	machine_child1, machine_child2 = singlePointCrossover(machine_parent1, machine_parent2, verge)

	#Multi Point Crossover
	pointsLength, points = 0, list()
	pointsLength = random.randint(chromosomeLength - 1)

	for x in range(random.randint(pointsLength)):
		X = random.rand(chromosomeLength - 1)
		while X in points:
			X = random.rand(chromosomeLength - 1)
		points.append(X)

	machine_child1, machine_child2 = multiPointCrossover(machine_parent1, machine_parent2, points)

	#Uniform Crossover
	P = np.random.rand(chromosomeLength)
	machine_child1, machine_child2 = uniformCrossover(machine_parent1, machine_parent2, P)

	return machine_child1, machine_child2
