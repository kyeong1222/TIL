#optimization for single variable

import scipy as sp
import scipy.optimize

def f1(x):
    return (x-2) ** 2 + 2

x0 = 0

result = sp.optimize.minimize(f1, x0)
print(result)


#optimization for dual variable

def f2(x):
    return (1 - x[0])**2 + 100.0 * (x[1] - x[0]**2)**2

x0_new = (2, 1)
result = optimize.minimize(f2, x0_new)
print(result)

#constrained optimization

def f1array(x):
    return x[0] ** 2 + x[1] ** 2


def eq_constraint(x):
    return x[0] + x[1] - 1


optimize.fmin_slsqp(f1array, np.array([1, 1]), eqcons=[eq_constraint])


