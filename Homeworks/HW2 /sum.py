import numpy as np
t = np.arange(0, np.pi + np.pi/30, np.pi/30)
y = np.cos(t)
S = np.sum(t * y)
print("the sum is:", S)
