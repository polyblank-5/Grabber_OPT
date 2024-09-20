import cvxpy as cp
import numpy as np

# solve for b,c,d,e l1*cos(a) = l4*cos(e)+l3*cos(e+d)+l2*cos(e+d+c), l1*cos(a)+l2*cos(a+b)=l4*cos(e)+l3*cos(e+d), l1*cos(a)+l2*cos(a+b)+l3*cos(a+b+c)=l4*cos(e), E = l1*cos(a)+l2*cos(a+b)+l3*cos(a+b+c)+l4*cos(a+b+c+d)

# Bhāskara I's sine approximation formula
'''um das convexe optimierungsproblem zu wird zu den vorhandenen Winkeln ein zusätzlicher variabler winkel hinzugenommen, 
um keine nicht lineare Funktionen zu verwenden wird dieser kleine variable WInkel linearisiert berechnet. Hier wird Bhāskara I's verwendet, 
da es eine quadratische approximation der trigonometrischen Funktionen ist, welche um 0 einen geringeren Fehler auffweist, als eine Taylor approximatiion.
http://datagenetics.com/blog/july12019/index.html

'''
def sin_approx(x):
    return 16*x*(np.pi-x) / (5*np.pi**2-4*x*(np.pi-x))

def cos_approx(x):
    return (np.pi**2-4*x**2) / (np.pi**2 + x**2)

def sin_add(x,y): # x ist const 
    return np.sin(x)* cos_approx(y) + np.cos(x) * sin_approx(y)

def cos_add(x,y):
    return np.cos(x)*cos_approx(y) -np.sin(x)*sin_approx(y)

l1 = 32.3932
l2 = 46.9224
l3 = 18.9208
l4 = 56.4341


alpha_const = 1
beta_const = 1
gamma_const = 1
delta_const = 1
epsilon_const = 1

alpha_1 = np.arcsin(l2/l4)
gamma_1 = np.arcsin(l1/l4)
alpha = cp.Variable(1)
beta = np.pi/2
delta = alpha-alpha_1
epsilon = np.pi-delta
gamma = gamma_1 + epsilon

p_A = np.array([0,0])
p_E = np.array([1,1]) # TODO: ändern zum richtigen Wert
p_B = cp.vstack([p_A[0] + l1*cos_add(alpha_const,alpha),p_A[1]+l1*sin_add(alpha_const,alpha)])
p_D = cp.vstack([p_E[0] + l4*cos_add(epsilon_const,epsilon),p_E[1] + l4*sin_add(epsilon_const,epsilon)])

#abs_BminusH = l2**2-l3**2+cp.norm(p_D-p_B)**2
#abs_CminusH = cp.sqrt(l2**2-abs_BminusH**2)
#p_H = p_B + abs_BminusH / cp.norm(p_B -p_D) * (p_D -p_B)

#p_C = np.array([p_H[0]+abs_CminusH/cp.norm(p_B - p_D) * (p_D[1]-p_B[1]),p_H[1] + abs_CminusH/cp.norm(p_B-p_D)* (p_D[0]-p_B[0])])