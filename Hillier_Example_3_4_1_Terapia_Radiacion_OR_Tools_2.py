# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:34:59 2021

@author: felipecas
"""

from __future__ import print_function
from ortools.linear_solver import pywraplp

def Terapiaderadiacion():
    '''Terapia de radiación. Ejemplo 3.4.1 Hillier'''
    
    #Declare the solver, naming it Terapiaderadiacion
    solver = pywraplp.Solver('Terapiaderadiacion',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    
    #Create the variables
    x1 = solver.NumVar(0, solver.infinity(), "x1")
    x2 = solver.NumVar(0, solver.infinity(), "x2")
    
    #Objective function
    objective = solver.Objective()
    objective.SetCoefficient(x1, 0.4)
    objective.SetCoefficient(x2, 0.5)
    objective.SetMinimization()

    #Add the constraints to the model
    
    #Constraint 1:
    constraint1 = solver.Constraint(-solver.infinity(), 2.7)
    constraint1.SetCoefficient(x1, 0.3)
    constraint1.SetCoefficient(x2, 0.1)
    
    #Constraint 2:
    constraint2 = solver.Constraint(6, 6)
    constraint2.SetCoefficient(x1, 0.5)
    constraint2.SetCoefficient(x2, 0.5)
    
    #Constraint 3:
    constraint3 = solver.Constraint(6, solver.infinity())
    constraint3.SetCoefficient(x1, 0.6)
    constraint3.SetCoefficient(x2, 0.4)
    
    #Solve the problem
    solver.Solve()
    opt_solution = 0.4*x1.solution_value() + 0.5*x2.solution_value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    
    #Print the value of each decision variable in the solution
    print('Solution: ')
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())
    
    #Print the value of the objective function in the solution
    print('Optimal objective value =', opt_solution)
    
Terapiaderadiacion()