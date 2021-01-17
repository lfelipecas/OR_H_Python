# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:34:59 2021

@author: felipecas
"""

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

#Create the model
model = LpProblem(name = "Wyndor_Glass_Co", sense = LpMaximize)

#Initialize the decision variables
x1 = LpVariable(name = "x1", lowBound = 0)
x2 = LpVariable(name = "x2", lowBound = 0)

#Add the constraints to the model
model += (x1 <= 4, "Plant 1")
model += (2*x2 <= 12, "Plant 2")
model += (3*x1 + 2*x2 <= 18, "Plant 3")

#Add the objective function to the model
model += lpSum([3*x1, 5*x2])

#Solve the problem
status = model.solve()

print(f"Status: {model.status}, {LpStatus[model.status]}")
print(f"Objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")
    
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
    
print(model.variables())
print(model.variables()[0] is x1)
print(model.variables()[1] is x2)
print(model.solver)