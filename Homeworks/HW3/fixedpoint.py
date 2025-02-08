import numpy as np
from types import LambdaType

def fixedpt(f: LambdaType, x0: int, tol: float, Nmax: int) -> list:
    count = 0
    while count < Nmax:
        count += 1
        x1 = f(x0)
        if abs(x1 - x0) < tol:
            return [x1, 0]
        x0 = x1
    return [x0, 1]


def driver():
    g = lambda x: -np.sin(2*x) + 5.0*x/4.0 - 3.0/4.0

    Nmax = 100
    tol = 1e-10

    guesses = [-1.0, 0.0, 2.0, 5.0, 7.0]

    for x0 in guesses:
        [xstar, ier] = fixedpt(g, x0, tol, Nmax)
        if ier == 0:
            print(f"Starting guess x0 = {x0:5.2f}  -->  converged to x* = {xstar:.14g}")
        else:
            print(f"Starting guess x0 = {x0:5.2f}  -->  did NOT converge (ier = {ier})")

if __name__ == "__main__":
    driver()

