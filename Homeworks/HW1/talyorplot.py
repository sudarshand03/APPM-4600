import numpy as np
import matplotlib.pyplot as plt

def direct_diff(x, delta):
    return np.cos(x + delta) - np.cos(x)

def product_diff(x, delta):
    return -2.0 * np.sin(x + 0.5*delta) * np.sin(0.5*delta)

def taylor_diff(x, delta):
    return -delta * np.sin(x) - 0.5*(delta**2) * np.cos(x)

x_values = [np.pi, 1e6]

deltas = np.logspace(-16, 0, 17)

for x in x_values:
    direct_errors = []
    taylor_errors = []

    for d in deltas:
        prod_val = product_diff(x, d)

        direct_val = direct_diff(x, d)
        direct_errors.append(abs(direct_val - prod_val))

        taylor_val = taylor_diff(x, d)
        taylor_errors.append(abs(taylor_val - prod_val))

    plt.figure()
    plt.loglog(deltas, direct_errors, 'o-', label='|direct - product|')
    plt.loglog(deltas, taylor_errors, 's-', label='|taylor - product|')
    plt.xlabel(r'$\delta$')
    plt.ylabel('Absolute difference')
    plt.title(f'Comparison for x = {x}')
    plt.grid(True, which='both')
    plt.legend()
    plt.show()
