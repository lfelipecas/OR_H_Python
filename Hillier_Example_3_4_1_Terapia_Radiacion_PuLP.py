# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:34:59 2021

@author: felipecas
"""

from pulp import LpMinimize, LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

#Create the model
model = LpProblem(name = "Terapia_Radiacion", sense = LpMinimize)

#Initialize the decision variables
x1 = LpVariable(name = "x1", lowBound = 0)
x2 = LpVariable(name = "x2", lowBound = 0)

#Add the constraints to the model
model += (0.3*x1 + 0.1*x2 <= 2.7, "Tejido critico")
model += (0.5*x1 + 0.5*x2 == 6, "Region del tumor")
model += (0.6*x1 + 0.4*x2 >= 6, "Centro del tumor")

#Add the objective function to the model
model += lpSum([0.4*x1, 0.5*x2])

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