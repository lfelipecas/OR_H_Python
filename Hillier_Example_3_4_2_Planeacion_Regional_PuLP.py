# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:34:59 2021

@author: felipecas
"""

from pulp import LpMinimize, LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

#Create the model
model = LpProblem(name = "Planeacion_Regional", sense = LpMaximize)

#Initialize the decision variables

x = {i: LpVariable(name=f"x{i}", lowBound = 0) for i in range(1, 10)}

# x1 = LpVariable(name = "x1", lowBound = 0)
# x2 = LpVariable(name = "x2", lowBound = 0)
# x3 = LpVariable(name = "x3", lowBound = 0)
# x4 = LpVariable(name = "x4", lowBound = 0)
# x5 = LpVariable(name = "x5", lowBound = 0)
# x6 = LpVariable(name = "x6", lowBound = 0)
# x7 = LpVariable(name = "x7", lowBound = 0)
# x8 = LpVariable(name = "x8", lowBound = 0)
# x9 = LpVariable(name = "x9", lowBound = 0)

#Add the constraints to the model

#Terreno para uso en cada kibbutz
model += (x[1] + x[4] + x[7] <= 400, "Kibbutz 1")
model += (x[2] + x[5] + x[8] <= 600, "Kibbutz 2")
model += (x[3] + x[6] + x[9] <= 300, "Kibbutz 3")

#Asignación de agua para cada kibbutz
model += (3*x[1] + 2*x[4] + x[7] <= 600, "Agua Kibbutz 1")
model += (3*x[2] + 2*x[5] + x[8] <= 800, "Agua Kibbutz 2")
model += (3*x[3] + 2*x[6] + x[9] <= 375, "Agua Kibbutz 3")

#Acres para cada cultivo
model += (x[1] + x[2] + x[3] <= 600, "Acres remolacha")
model += (x[4] + x[5] + x[6] <= 500, "Acres algodón")
model += (x[7] + x[8] + x[9] <= 325, "Acres sorgo")

#Proporción de área plantada
model += (3*(x[1] + x[4] + x[7]) - 2*(x[2] + x[5] + x[8]) == 0, "Kibbutz 1 y 2")
model += ((x[2] + x[5] + x[8]) - 2*(x[3] + x[6] + x[9]) == 0, "Kibbutz 2 y 3")
model += (4*(x[3] + x[6] + x[9]) - 3*(x[1] + x[4] + x[7]) == 0, "Kibbutz 3 y 1")


#Add the objective function to the model
model += 1000*(x[1] + x[2] + x[3]) + 750*(x[4] + x[5] + x[6]) + 250*(x[7] + x[8] + x[9])

#Solve the problem
status = model.solve()

print(f"Status: {model.status}, {LpStatus[model.status]}")
print(f"Objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")
    
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
    
print(model.variables())
print(model.variables()[0] is x[1])
print(model.variables()[1] is x[2])
print(model.variables()[2] is x[3])
print(model.variables()[3] is x[4])
print(model.variables()[4] is x[5])
print(model.variables()[5] is x[6])
print(model.variables()[6] is x[7])
print(model.variables()[7] is x[8])
print(model.variables()[8] is x[9])
print(model.solver)