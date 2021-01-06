from sys import stdin
from itertools import combinations
from numpy import product
from numpy.core.fromnumeric import prod

l = [int(x) for x in stdin.read().split('\n')]


def ideal_quantum_entanglement(boxes, groups):

    group_size = sum(boxes) // groups

    for i, box in enumerate(boxes):

        if qes := [product(c) for c in combinations(boxes, i) if sum(c) == group_size]:
            return min(qes)

# Part One
print(ideal_quantum_entanglement(l, 3))

# Part Two
print(ideal_quantum_entanglement(l, 4))
