# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:34:59 2021

@author: felipecas
"""

from __future__ import print_function
from ortools.linear_solver import pywraplp

def WyndorGlassCo():
    """Wyndor Glass Co"""
    #Initiate a Glop solver, naming it WyndorGlassCo
    solver = pywraplp.Solver('WyndorGlassCo',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    
    #Create the two decision variables and let them take on non negative real values
    x1 = solver.NumVar(0, solver.infinity(), "x1")
    x2 = solver.NumVar(0, solver.infinity(), "x2")
    
    #Objective function
    objective = solver.Objective()
    objective.SetCoefficient(x1, 3)
    objective.SetCoefficient(x2, 5)
    objective.SetMaximization()

    #Add the constraints to the model
    
    #Constraint 1: Plant 1 constraint
    constraint1 = solver.Constraint(-solver.infinity(), 4)
    constraint1.SetCoefficient(x1, 1)
    constraint1.SetCoefficient(x2, 0)
    
    #Constraint 2: Plant 2 constraint
    constraint2 = solver.Constraint(-solver.infinity(), 12)
    constraint2.SetCoefficient(x1, 0)
    constraint2.SetCoefficient(x2, 2)
    
    #Constraint 3: Plant 3 constraint
    constraint3 = solver.Constraint(-solver.infinity(), 18)
    constraint3.SetCoefficient(x1, 3)
    constraint3.SetCoefficient(x2, 2)
    
    #Solve the problem
    solver.Solve()
    opt_solution = 3*x1.solution_value() + 5*x2.solution_value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    
    #Print the value of each decision variable in the solution
    print('Solution: ')
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())
    
    #Print the value of the objective function in the solution
    print('Optimal objective value =', opt_solution)
    
WyndorGlassCo()