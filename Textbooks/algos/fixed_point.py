from typing import Callable, Tuple
import numpy as np


class FixedPoint:
    def __init__(self,
                 func: Callable[[float], float],
                 initial_guess: float,
                 max_iterations: int,
                 tolerance: float = 1e-7) -> None:
        """
        Constructor fixed point iteration solver

        :param func: function to find fixed point (solve x = g(x))
        :param intial_guess: inital guess of fixe point (x_0)
        :param tolerance: convergence error tolerance
        :param max_iter: Max number of iterations allowed before failure
        """
        self.func: Callable[[float], float] = func
        self.inital_guess: float = initial_guess
        self.tolerance: float = tolerance
        self.max_iterations: int = max_iterations

    def solve(self) -> Tuple[float, bool, int]:
        """
        Perform fixed point iteration to find approximate g(p) = p

        :return : A tuple contiaing:
            - Approx fixed point
            - Error flag
            - Number of iterations
        """

        #cumsum number of iterations
        iterations: int = 0

        #inital guess of fixed points
        x_current = self.inital_guess


        while iterations < self.max_iterations:
            #update fixed point sequence
            x_next = self.func(x_current)

            # |p-p_0| < Tol return p
            if abs(x_next - x_current) < self.tolerance:
                return (x_next, False, iterations)

            #update fixed point sequence
            x_current = x_next

        return (x_current, True, iterations)


if __name__ == "__main__":

    #Example usage

    g = lambda x : np.cos(x)
    initial_guess = 0.5
    max_iterations = 100

    solver = FixedPoint(g, initial_guess, max_iterations)
    fixed_point, error_flag, iterations = solver.solve()

    print("Approximate fixed point:", fixed_point)
    print("Error flag (False means success):", error_flag)
    print("Iterations:", iterations)

