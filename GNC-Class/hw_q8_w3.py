import sympy as sp
import matplotlib.pyplot as plt
from numpy import *
import numpy as np

def calc_integral_analytics(matrix, index):
    t = sp.Symbol('t')
    omega = np.array([[20 * sp.sin(0.1 * t)],
                      [20 * 0.01 * t],
                      [20 * sp.cos(0.1 * t)]])

    beta_dot = np.dot(mx_beta[index, : ], omega)
    print(beta_dot)
    sp.integrate(beta_dot, t)


def calc_integral_numeric(t, matrix, index):
    omega = np.array([[20 * sp.sin(0.1 * t)],
                      [20 * 0.01 * t],
                      [20 * sp.cos(0.1 * t)]])

    beta_dot = np.dot(mx_beta[index, : ], omega)
    return beta_dot

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
calc_integral_analytics(mx_beta, index)
