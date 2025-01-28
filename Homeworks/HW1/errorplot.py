import numpy as np
import matplotlib.pyplot as plt


exponents = np.arange(-16, 1)  
deltas = 10.0 ** exponents   

def direct_diff(x, delta):
    return np.cos(x + delta) - np.cos(x)

def identity_diff(x, delta):
    return -2.0 * np.sin(x + delta/2.0) * np.sin(delta/2.0)

def compare_cos_diffs(x_value):
    direct_vals = []
    identity_vals = []
    
    for d in deltas:
        d_direct = direct_diff(x_value, d)
        d_id = identity_diff(x_value, d)
        
        direct_vals.append(d_direct)
        identity_vals.append(d_id)
    
    direct_vals = np.array(direct_vals)
    identity_vals = np.array(identity_vals)
    
    diff = identity_vals - direct_vals
    
    abs_diff = np.abs(diff)
    
    plt.figure(figsize=(7,5))
    plt.plot(deltas, abs_diff, marker='o')
    
    plt.xscale('log')  
    plt.yscale('log') 
    
    plt.title(f"Absolute difference between identity-based and direct for x = {x_value}")
    plt.xlabel("delta (log scale)")
    plt.ylabel("|cos-identity - cos-direct| (log scale)")
    plt.grid(True, which="both", ls=":")
    plt.show()

x_values = [np.pi, 1e6]

for x_val in x_values:
    compare_cos_diffs(x_val)

