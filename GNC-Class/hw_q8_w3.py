import matplotlib.pyplot as plt
from numpy import *
from scipy import integrate
import numpy as np


def calc_integral_numeric(y, t):
    mx_beta_array = np.array([[ -y[1],  -y[2],  -y[3]],
                        [  y[0],  -y[3],   y[2]],
                        [  y[3],   y[0],  -y[1]],
                        [ -y[2],   y[1],   y[0]]])
    omega = np.array([0.349066 * np.sin(0.1 * t),
                      0.349066 * 0.01,
                      0.349066 * np.cos(0.1 * t)])

    beta_dot = 1/2*np.dot(mx_beta_array,omega.transpose())
    print(beta_dot.transpose())
    return beta_dot


beta0 = 0.408248
beta1 = 0
beta2 = 0.408248
beta3 = 0.816497

y0 = np.array([beta0, beta1, beta2, beta3])


# Numeric Form

t = np.linspace(0, 60, 101)
values = integrate.odeint(calc_integral_numeric, y0, t)


# for i in range(0,len(b0_vector)):
#     print(b0_vector[i]*b0_vector[i] + b1_vector[i]*b1_vector[i] + b2_vector[i]*b2_vector[i] + b3_vector[i]*b3_vector[i])

plt.plot(t, values)
plt.legend(['b0', 'b1', 'b2', 'b3'])
plt.grid()
plt.ylim([-1,1])
plt.ylabel('Quaternions')
plt.xlabel('Time[sec]')
plt.show()

