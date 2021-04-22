import random
import numpy as np 
import pandas as pd 
import time 
import math

def string(Y, X):
	return ['J{}'.format((X + 1) * 10 + Y[X] + 1)]

def fitness(paramters):
	jobs = paramters[0],
	machines = paramters[1],
	operations = paramters[2],
	operation_vector = paramters[3],
	machine_vector = paramters[4], 
	operational_cost = paramters[5]

    job_time, machine_time, buffer_tasks, regans, cost = [0] * jobs, [0] * machines, [0] * jobs, [list()] * machines, 0

    for task in operation_vector:
        job = task - 1; op = buffer_tasks[job]
        
        m_index = operations * job + op; machine = machine_vector[m_index] - 1
        time = max(job_time[job], machine_time[machine])
        
        added = operational_cost[operations * job + op][machine]

        for i in range(machine_time[machine], time): regans[machine] = regans[machine] + [0]
            
        for i in range(time, time + added):
            regans[machine] += string(buffer_tasks, job)

        machine_time[machine] = len(regans[machine])
        job_time[job] = len(regans[machine]); buffer_tasks[job] += 1

    for machine in range(machines): cost = max(cost, len(regans[machine]))

    return (cost, regans)
