"""
Author: Dr.Moumita Deb
This code are used for solution of Fuzzy multiobjective linear fractional programming problems
"""

# Import all classes of PuLP module
from pulp import *

# Create the problem variable to contain the problem data
model = LpProblem("Max-min problem", LpMaximize)

# Create 4 variables

y1 = LpVariable("variable 1", 0, None, LpInteger)
y2 = LpVariable("variable 2", 0, None, LpInteger)
t = LpVariable("variable 3", 0, None, LpInteger)
z = LpVariable("variable 4", 0, None, LpInteger)


# Create maximize objective function
model += z
# Create fourteen  constraints
model += 1 * y1 + 1 * y2 + 3 * t <= 5.00, "C1"
model += 1 * y1 + 1 * y2 + 3 * t - 3.68 * z >= 1.32, "C2"
model += 7 * y1 + 2 * y2 <= 35.00, "C3"
model += 7 * y1 + 2 * y2 - 33.6 * z >= 1.40, "C4"
model += 1 * y1 + 1 * y2 + 1 * t >= 1, "C5"
model += 1 * y1 + 1 * y2 + 1 * t + 4 * z  <= 5, "C6"
model += 2 * y1 + 3 * y2 - 15 * t >= 1, "C7"
model += 2 * y1 + 3 * y2 - 15 * t + 14 * z <= 15, "C8"
model += -1 * y1 + 3 * t  >= 1, "C9"
model += -1 * y1 + 3 * t + 24 * z <= 25, "C10"
model += 5 * y1 + 2 * y2  + 1 * t  >= 1, "C11"
model += 5 * y1 + 2 * y2 + 1 * t + 34 * z <= 35, "C12"
model += 3 * y1 - 2 * y2  >= 1, "C13"
model += 3 * y1 - 2 * y2 + 49 * z <= 50, "C14"

# The problem is solved using PuLP's choice of Solver
model.solve()

# Each of the variables is printed with it's resolved optimum value
for v in model.variables():
    print(v.name, "=", v.varValue)
