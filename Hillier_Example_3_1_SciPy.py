# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:34:59 2021

@author: felipecas
"""

from scipy.optimize import linprog

obj = [-3, -5]

lhs_ineq = [[1, 0], [0, 2], [3, 2]]

rhs_ineq = [4, 12, 18]

bnd = [(0, float("inf")), (0, float("inf"))]

opt = linprog(c = obj, A_ub = lhs_ineq, b_ub = rhs_ineq,
              method = "revised simplex")

opt

print(opt.fun)
print(opt.success)
print(opt.x)