import math
from statistics import median, stdev

from numpy import average
from scipy.optimize import fsolve
from itertools import combinations




tolerance = 1e-7
d = 127

# Data points (x, y)
points = [
    [1, 140], [2, 171], [3, 190],
    [4, 201], [5, 213], [6, 227],
    [7, 246], [8, 274], [9, 300],
    [10, 350], [11, 430], [12, 566],
    [13, 682]
]

possibilities = list(combinations(points, 3))
def equations(vars, subset):
    a, b, c = vars
    return [a * (x ** 3) + b * (x ** 2) + c * x + d - y for x, y in subset]

def calculate_goodness(a, b, c, x, y):
    skibidiY = a * x ** 3 + b * x ** 2 + c * x + d
    meow = abs(skibidiY - y)
    return meow


solutions = []

# Solve for each subset
for subset in possibilities:
    try:
        a, b, c = fsolve(equations, [1, 1, 1], args=(subset,))
        solutions.append((a, b, c))
    except RuntimeError:
        continue


stuff = {}
for i, (a, b, c) in enumerate(solutions):
    good_points = []
    goodnesses = []
    for j in points:
        hmmm = calculate_goodness(a, b, c, j[0], j[1])
        goodnesses.append(hmmm)
        if math.isclose(hmmm, 0, abs_tol=tolerance):
            good_points.append([j[0], j[1]])
        goodnesses.append(hmmm)

    deviation = float(stdev(goodnesses))
    stuff[deviation] = [float(a), float(b), float(c), good_points, average(goodnesses)]



stuff = dict(sorted(stuff.items()))

first = 500
for i, j in stuff.items():
    first-=1
    if first == 0:
        break
    print(f"stdev: {i}, a = {j[0]}, b = {j[1]}, c = {j[2]} good_points = {j[3]}, average = {j[4]}")


