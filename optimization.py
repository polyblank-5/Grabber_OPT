import cvxpy as cp
import numpy as np

# solve for b,c,d,e l1*cos(a) = l4*cos(e)+l3*cos(e+d)+l2*cos(e+d+c), l1*cos(a)+l2*cos(a+b)=l4*cos(e)+l3*cos(e+d), l1*cos(a)+l2*cos(a+b)+l3*cos(a+b+c)=l4*cos(e), E = l1*cos(a)+l2*cos(a+b)+l3*cos(a+b+c)+l4*cos(a+b+c+d)

l1 = 32.3932
l2 = 46.9224
l3 = 18.9208
l4 = 56.4341

alpha_1 = np.arcsin(l2/l4)
gamma_1 = np.arcsin(l1/l4)
alpha = cp.Variable(1)
beta = np.pi/2
delta = alpha-alpha_1
epsilon = np.pi-delta
gamma = gamma_1 + epsilon

p_B = [l1*np.cos(alpha),l1*np.sin(alpha)]
p_D = [l4*np.cos(epsilon),l4*np.sin(epsilon)]

 = 

p_C = 