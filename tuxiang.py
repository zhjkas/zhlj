import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def function(x, a):
    return np.exp(-a/4)*np.exp(-x**2*a)*(2*np.pi*x)*(np.sinh(np.pi)/np.cosh(np.pi*x)**2)


def integrate_function(x_min, x_max, a):
    return integrate.quad(function, x_min, x_max, args=(a,))[0]


# define integration range
x_min = 0
x_max = 1
# define range of a variable
a_points = np.linspace(0, 10, 100)

results = []
for a in a_points:
    value = integrate_function(x_min, x_max, a)
    results.append(value)


plt.plot(a_points, results)
plt.ylabel("Integral value")
plt.xlabel("a variable")
plt.show()
