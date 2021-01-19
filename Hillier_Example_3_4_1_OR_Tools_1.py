# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:34:59 2021

@author: felipecas
"""

# Import the linear solver
from ortools.linear_solver import pywraplp

def Terapiaderadiacion():
    '''Terapia de radiación. Ejemplo 3.4.1 Hillier'''

    # Declare the solver
    solver = pywraplp.Solver('Terapiaderadiacion',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    
    #Create the variables
    x1 = solver.NumVar(0, solver.infinity(), 'x1')
    x2 = solver.NumVar(0, solver.infinity(), 'x2')
    
    print('Number of variables =', solver.NumVariables())
    
    # Define the objective function
    solver.Minimize(0.4*x1 + 0.5*x2)
    
    # Define the constraints
    solver.Add(0.3*x1 + 0.1*x2 <= 2.7)
    solver.Add(0.5*x1 + 0.5*x2 == 6)
    solver.Add(0.6*x1 + 0.4*x2 >= 6)
    
    # Invoke the solver
    status = solver.Solve()
    
    # Display the solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution')
        print('Objective value =', solver.Objective().Value())
        print('x1 =', x1.solution_value())
        print('x2 =', x2.solution_value())
    else:
        print('The problem does not have an optimal solution.')
    
    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' %solver.wall_time())
    print('problem solved in %d iterations' %solver.iterations())
    print('problem solved in %d branch-and-bound nodes' %solver.nodes())

Terapiaderadiacion()