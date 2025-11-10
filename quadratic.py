import math
from itertools import combinations
from statistics import stdev

from scipy.optimize import fsolve

# d = 633
tolerance = 1e-7

points = [
    [14, 655],
    [15, 633],
    [16, 660],
    [17, 685],
    [18, 716],
    [19, 765],
    [20, 818],
    [21, 859],
    [22, 926],
    [23, 1004],
    [24, 1076],
    [25, 1143],
    [26, 1277],
    [27, 1373],
    [28, 1537],
]


possibilities = list(combinations(points, 3))

def equations(vars, subset):
    a, b, d = vars
    return [a * (x ** 2) + b * x + d - y for x, y in subset]

def calculate_goodness(a, b, x, y, d):
    skibidiY = a * x ** 2 + b * x + d
    meow = abs(skibidiY - y)
    return meow

solutions = []

for subset in possibilities:
    try:
        a, b, d = fsolve(equations, [1, 1, 1], args=(subset,))
        solutions.append((a, b, d))
    except RuntimeError:
        continue



stuff = {}
for i, (a, b, d) in enumerate(solutions):
    good_points = []
    goodnesses = []
    for j in points:
        hmmm = calculate_goodness(a, b, j[0], j[1], d)

        if math.isclose(hmmm, 0, abs_tol=tolerance):
            good_points.append([j[0], j[1]])
        goodnesses.append(hmmm)
    deviation = float(stdev(goodnesses))
    stuff[deviation] = [float(a), float(b), good_points, d]

stuff = dict(sorted(stuff.items()))


first = 500
for i, j in stuff.items():
    first-=1
    if first == 0:
        break
    print(f"stdev: {i}, a = {j[0]}, b = {j[1]}, good_points = {j[2]}, d = {j[3]}, index = {500-first}")
