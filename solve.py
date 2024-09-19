from sympy import solve, cos, sin
from sympy.abc import a,b,c,d,e,alpha,beta,gamma,delta,epsilon,w,x,y,z
import numpy as np

"""
alpha = alpha x0 alpha
beta = beta x1
gamma = gamma x2
delta = delta x3
epsilon = epsilon x4
w = w
x = x
y = y
z = z
"""
equation = [
-w*(sin(a)+cos(a)*alpha)+z*(sin(e)+cos(e)*epsilon)+y*(sin(d+e)*(1-epsilon*delta)+cos(d+e)*(delta+epsilon))+x*(sin(c+d+e)*(1-delta*epsilon-epsilon*gamma-gamma)+cos(c+d+e)*(epsilon+delta+gamma-epsilon*gamma)),
w*(sin(a)+cos(a)*alpha) + x*(sin(a+b)*(1-alpha*beta)+cos(a+b)*(beta+alpha)) - z*(sin(e)+cos(e)*epsilon)-y*(sin(d+e)*(1-epsilon*delta)+cos(d+e)*(delta+epsilon)),
w*(sin(a)+cos(a)*alpha) + x*(sin(a+b)*(1-alpha*beta)+cos(a+b)*(beta+alpha)) + y*(sin(a+b+c)*(1-alpha*beta-alpha*gamma-gamma)+cos(a+b+c)*(alpha+beta+gamma-alpha*gamma))-z*(sin(e)+cos(e)*epsilon),
a+b+c+d+e+alpha+beta+gamma+delta+epsilon-3*np.pi
]
solutions = solve(equation,[beta,gamma,delta,epsilon],dict=True)
print(solutions)
print("solved")