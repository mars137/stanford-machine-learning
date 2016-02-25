# -*- coding: utf-8 -*-
import math
import numpy as NP

# β is probability of following the link
b = 0.7

# M is the matrix of vectors based on the schma of exercice
M = NP.matrix([[0, 0, 0], [1/2, 0, 0], [1/2, 1, 1]])

# r is the list of node we are applying the M on every iteration
r = NP.matrix([1/3, 1/3, 1/3]).T

# S represent the change that the user doesn't follow the link but jump to a random link
S = NP.matrix([(1 - b)/3, (1 - b)/3, (1 - b)/3]).T

# 𝛆 is the choosen Pagerank precision
e = 1 / 10000

def power_iteration(r):
    r_copy = r
    # Calculate new values for r
    r = b * M * r
    # Add the leaking rank due to the probably that user may not follow the link
    r = r + S
    
    # Pagerank is processed when no value changed more than 𝛆 on this iteration
    matrix_difference = r_copy - r
    is_processed = math.fabs(matrix_difference.max()) < e
    return (r, is_processed)

# Execute power interation until the Pagerank is processed
while True:
    r, is_processed = power_iteration(r)
    if is_processed:
        print("Pagerank processed!")
        break

# Multiply the Pagerank by 3 because "the sum of the PageRanks of the three pages must be 3"        
r = 3 * r

# Print result to solve exercice
a = r.flat[0]
b = r.flat[1]
c = r.flat[2]
print("a + c = {0}".format(round(a + c, 3)))
print("b + c = {0}".format(round(b + c, 3)))