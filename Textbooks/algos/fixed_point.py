from typing import Callable, Tuple
import numpy as np


class FixedPoint:
    def __init__(self,
                 func: Callable[[float], float],
                 initial_guess: float,
                 max_iterations: int,
                 tolerance: float = 1e-7,
                 contraction_factor: float = None) -> None:
        """
        Constructor fixed point iteration solver

        :param func: function to find fixed point (solve x = g(x))
        :param intial_guess: inital guess of fixe point (x_0)
        :param tolerance: convergence error tolerance
        :param max_iter: Max number of iterations allowed before failure
        :param contraction_factor: Optional use Lipschitz constant L for g if (0<=L<=1)
            -L found analytically
        """
        self.func: Callable[[float], float] = func
        self.inital_guess: float = initial_guess
        self.tolerance: float = tolerance
        self.contraction_factor: float = contraction_factor
        self.max_iterations: int = max_iterations

        #intial difference |p_1-p_0| for error bound
        self.intial_diff: float = None

    def solve(self) -> Tuple[float, bool, int]:
        """
        Perform fixed point iteration to find approximate g(p) = p

        :return : A tuple contiaing:
            - Approx fixed point
            - Error flag
            - Number of iterations
        """

        # cumsum number of iterations
        iterations: int = 0

        # inital guess of fixed points
        x_current = self.inital_guess

        while iterations < self.max_iterations:
            # update fixed point sequence
            x_next = self.func(x_current)
            iterations += 1
            
            #record first difference for error bound
            if iterations == 1:
                self.intial_diff = abs(x_next - x_current)

            # |p-p_0| < Tol return p
            if abs(x_next - x_current) < self.tolerance:
                return (x_next, False, iterations)

            # update fixed point sequence
            x_current = x_next

        return (x_current, True, iterations)

    def error_bound(self, iterations: int) -> float:
        """
        Compute Theoretical error bound for fixed point iteration after n iterations of fixed point method

        Implments contraction mapping theorem error

        |p_n-p| <= ((L^n)/(1-L)) * |p_1 - p_0|
        """
        if self.contraction_factor is None:
            raise ValueError ("Provide Contraction Factor")
        if self.intial_diff is None:
            raise ValueError("Record Intial difference first, run solve()")
        
        L = self.contraction_factor

        if L >=1 or L <=0:
            raise ValueError (" L needs to be in between 0 and 1")

        n = iterations
        return ((L**n)/(1-L))**self.intial_diff

if __name__ == "__main__":

    # Example usage

    g = lambda x: np.cos(x)

    initial_guess = 0.5
    max_iterations = 100

    #g(x) = cos(x) -> g'(x) = sin(x) -> |g'(x)| <=1 for x choose L=0.8

    contraction_factor = 0.8

    tolerance = 1e-7

    solver = FixedPoint(g, initial_guess, max_iterations, tolerance, contraction_factor)
    fixed_point, error_flag, iterations = solver.solve()

    print("Approximate fixed point:", fixed_point)
    print("Error flag (False means success):", error_flag)
    print("Iterations:", iterations)

    try:
        bound = solver.error_bound(iterations)
    except ValueError as e:
        bound = None
        print("Error computing error bound:", e)

    if bound is not None:
        print("Theoretical error bound after", iterations, "iterations is :", bound)
