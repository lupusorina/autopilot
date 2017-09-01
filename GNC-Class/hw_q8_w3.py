from sympy import *
import matplotlib.pyplot as plt
from numpy import *
import numpy as np

def fct(matrix, index):
    t = Symbol('t')
    omega = np.array([[20 * np.sin(0.1 * t)],
                      [20 * 0.01 * t],
                      [20 * np.cos(0.1 * t)]])

    beta_dot = np.dot(mx_beta[index, : ], omega)
    print(beta_dot)
    integrate(beta_dot, t)

    return test1

beta0 = 0.408248
beta1 = 0
beta2 = 0.408248
beta3 = 0.816497


mx_beta = array([[ -beta1,  -beta2,  -beta3],
                [  beta0,  -beta3,   beta2],
                [ -beta3,   beta0,  -beta1],
                [ -beta2,   beta1,   beta0]])

#print (beta0*beta0 + beta1*beta1 + beta2*beta2 + beta3*beta3)

index = 0
fcn(mx_beta, index)
