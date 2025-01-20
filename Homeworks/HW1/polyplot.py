import numpy as np
import matplotlib.pyplot as plt

x_vals = np.arange(1.920, 2.081, 0.001)
coeffs = [1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512]

polyval_coeffs = np.polyval(coeffs, x_vals)
polyval_fact = (x_vals - 2) ** 9

#Coefficent Plot
plt.figure(figsize=(8, 6))
plt.plot(x_vals, polyval_coeffs, 'b-')
plt.title("Plot of $p(x)$ using Expanded Coefficients")
plt.xlabel("x")
plt.ylabel("$p(x)$")
plt.grid(True)
plt.legend()
plt.show()


#Factorized Plot
plt.figure(figsize=(8, 6))
plt.plot(x_vals, polyval_fact, 'r-')
plt.title("Factorized Evaluation $(x-2)^9$")
plt.xlabel("x")
plt.ylabel("$p(x)$")
plt.grid(True)
plt.legend()
plt.show()
