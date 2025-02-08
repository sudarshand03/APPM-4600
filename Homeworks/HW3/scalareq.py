import numpy as np
import matplotlib.pyplot as plt

#-----------------------------
# PART (a): Plot f(x) = x - 4 sin(2x) - 3
#-----------------------------
def f(x):
    return x - 4*np.sin(2*x) - 3

# Plot over an interval that clearly contains all roots
xvals = np.linspace(-2, 8, 1000)
fvals = f(xvals)

plt.axhline(0, color='k', linestyle='--', linewidth=0.75)
plt.plot(xvals, fvals, label=r'$f(x) = x - 4\sin(2x) - 3$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x - 4 sin(2x) - 3')
plt.grid(True)
plt.legend()
plt.show()

# A quick way to guess the number of roots:
# Count sign-changes on the plotting grid.
num_roots_est = 0
for i in range(len(xvals) - 1):
    if fvals[i] * fvals[i+1] < 0:
        num_roots_est += 1

print(f"Estimated number of roots (by sign changes): {num_roots_est}")
