import numpy as np
import matplotlib.pyplot as plt
import random

theta = np.linspace(0, 2*np.pi, 400)

R, dr, f, p = 1.2, 0.1, 15, 0

x = R * (1 + dr * np.sin(f * theta + p)) * np.cos(theta)
y = R * (1 + dr * np.sin(f * theta + p)) * np.sin(theta)
plt.figure()
plt.plot(x, y)
plt.title("Wavy Circle")
plt.show()


plt.figure()
for i in range(1, 11):
    R = i         
    dr = 0.05      
    f = 2 + i       
    p = random.uniform(0, 2)  
    x = R * (1 + dr * np.sin(f * theta + p)) * np.cos(theta)
    y = R * (1 + dr * np.sin(f * theta + p)) * np.sin(theta)
    plt.plot(x, y)
plt.title("10 Wavy Circles")
plt.show()