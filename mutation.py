import random
import numpy as np 

def check(X, Y, V):
	return Y == X or V[X] == V[Y]

def swap(V, X, Y):
	V[X], V[Y] = V[Y], V[X]

def operationalMutation(operation_vector, machine_vector, index, size):
    post_mutation_vector, target = operation_vector.copy(), index
    while check(index, target, post_mutation_vector): target = random.randrange(size)

    post_mutation_vector = swap(post_mutation_vector, index, target)
    return post_mutation_vector

def machineMutation(machine_vector, operation_vector, index, size):
    post_mutation_vector, target = machine_vector.copy(), index

    ta = pos
    while check(index, target, post_mutation_vector): target = random.randrange(size)
    post_mutation_vector = swap(post_mutation_vector, index, target)
    
    return post_mutation_vector
