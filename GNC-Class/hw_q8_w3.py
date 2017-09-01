import sympy as sp
import matplotlib.pyplot as plt
from numpy import *
from scipy import integrate
import numpy as np

def calc_integral_analytics(mx_beta, index):
    t = sp.Symbol('t')
    omega = sp.Matrix([[0.349066 * sp.sin(0.1 * t)],
                      [0.349066 * 0.01],
                      [0.349066 * sp.cos(0.1 * t)]])

    beta_dot = 1/2*mx_beta[index, : ] * omega
    return sp.integrate(beta_dot, t)[0, 0]


def calc_integral_numeric(t, mx_beta_array, index):
    omega = np.array([[0.349066 * sp.sin(0.1 * t)],
                      [0.349066 * 0.01],
                      [0.349066 * sp.cos(0.1 * t)]])
    beta_dot = 1/2*np.dot(mx_beta_array[index, : ],omega)
    print(index)
    return beta_dot


beta0 = 0.408248
beta1 = 0
beta2 = 0.408248
beta3 = 0.816497


mx_beta = sp.Matrix([[ -beta1,  -beta2,  -beta3],
                    [  beta0,  -beta3,   beta2],
                    [  beta3,   beta0,  -beta1],
                    [ -beta2,   beta1,   beta0]])

mx_beta_array = np.array([[ -beta1,  -beta2,  -beta3],
                        [  beta0,  -beta3,   beta2],
                        [  beta3,   beta0,  -beta1],
                        [ -beta2,   beta1,   beta0]])

# Analytic Form
b0 = calc_integral_analytics(mx_beta, index = 0)
b1 = calc_integral_analytics(mx_beta, index = 1)
b2 = calc_integral_analytics(mx_beta, index = 2)
b3 = calc_integral_analytics(mx_beta, index = 3)

print(b0)
print(b1)
print(b2)
print(b3)


# Numeric Form

time = np.arange(0, 200, 5)
def F(x, matrix, index):
    return integrate.quad(calc_integral_numeric, 0, x, args=(matrix, index))

b0_vector = [F(t, mx_beta_array, index=0)[0] for t in time]
b1_vector = [F(t, mx_beta_array, index=1)[0] for t in time]
b2_vector = [F(t, mx_beta_array, index=2)[0] for t in time]
b3_vector = [F(t, mx_beta_array, index=3)[0] for t in time]

# for i in range(0,len(b0_vector)):
#     print(b0_vector[i]*b0_vector[i] + b1_vector[i]*b1_vector[i] + b2_vector[i]*b2_vector[i] + b3_vector[i]*b3_vector[i])

plt.plot(time, b0_vector)
plt.plot(time, b1_vector)
plt.plot(time, b2_vector)
plt.plot(time, b3_vector)
plt.legend(['b0', 'b1', 'b2', 'b3'])
plt.ylabel('Quaternions')
plt.xlabel('Time[sec]')
plt.show()

