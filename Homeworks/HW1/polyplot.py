import numpy as np
import matplotlib.pyplot as plt

x_vals = np.arange(1.920, 2.081, 0.001)
coeffs = [1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512]

polyval_coeffs = np.polyval(coeffs, x_vals)
polyval_fact = (x_vals - 2) ** 9

plt.figure(figsize=(8, 6))
plt.plot(x_vals, polyval_coeffs, 'b-', label="Expanded $p(x)$")
plt.plot(x_vals, polyval_fact, 'r-', label="Factorized $(x-2)^9$")
plt.title("Comparison of Expanded and Factorized Polynomial")
plt.xlabel("x")
plt.ylabel("$p(x)$")
plt.grid(True)
plt.legend()
plt.show()
