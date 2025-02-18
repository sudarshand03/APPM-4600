from typing import Callable, Tuple, Optional
import numpy as np


class NewtonMethods:
    def __init__(self,
                 func: Callable[[float], float],
                 derivative: Optional[Callable[[float], float]],
                 initial_guess: float,
                 tolerance: float,
                 max_iterations: int) -> None:
        """
        Initialize the Newton's method solver (single variable)

        Implmentations of Newton-Raphson, LazyNewton (Chord Iteration), and Secant

        :param func: The function f(x) whose root we want to find.
        :param initial_guess: The starting value x0.
        :param tolerance: The convergence tolerance.
        :param max_iterations: Maximum number of iterations allowed.
        :param derivative: (Optional) The analytical derivative f'(x) of f.
                           If not provided, the derivative will be computed numerically.
        """
        self.f: Callable[[float], float] = func

        self.f_prime: Optional[Callable[[float], float]
                               ] = derivative  # May be none for secant

        self.initial_guess: float = initial_guess
        self.tolerance: float = tolerance
        self.max_iterations: int = max_iterations

    def newton_raphson(self, error_flag: bool = True) -> Tuple[float, bool, int]:
        """
        Perform Standard Newton-Raphson:
        x_{n+1} = x_n - f(x_n)/f'(x_n)

        :return : A tuple containg
            - Approximate Root
            - Error Flag
                - False if Tolerance was met
                - True if Max Iterations was hit (Failure), or division by 0
            - Number of Iterations
        """
        if self.f_prime is None:
            raise ValueError("Input Derivative for Newton-Raphson")

        # x_0
        x_current = self.initial_guess
        iterations = 0

        while iterations <= self.max_iterations:
            f_val = self.f(x_current)
            f_deriv = self.f_prime(x_current)

            if f_deriv == 0:
                # Avoid division by 0
                return (x_current, error_flag, iterations)
            iterations += 1

            # x_{n+1} = x_n - f(x_n)/f'(x_n)
            x_next = x_current - f_val/f_deriv

            if abs(x_next - x_current) < self.tolerance:
                error_flag = False
                return (x_next, error_flag, iterations)

            # iterate sequence
            x_current = x_next

        return (x_current, error_flag, iterations)

    def lazy_newton(self, error_flag: bool = True) -> Tuple[float, bool, int]:
        """
        Lazy Newton (Chord Iteration):

        x_{n+1} = x_n - f(x_n)/f'(x_0)
        """
        if self.f_prime is None:
            raise ValueError("Input Derivative for Lazy Newton")

        # x_0
        x_current = self.initial_guess

        # f'(x_0)
        deriv = self.f_prime(self.initial_guess)

        if deriv == 0:
            raise ValueError("Pick a different guess")

        iterations = 0

        while iterations < self.max_iterations:
            # x_{n+1} = x_n - f(x_n)/f'(x_0)
            x_next = x_current - self.f(x_current) / deriv

            # update iterations
            iterations += 1

            # check it sequence converged within tolerance
            if abs(x_next - x_current) < self.tolerance:
                error_flag = False
                return (x_next, error_flag, iterations)

            # iterate sequence
            x_current = x_next

        return (x_current, error_flag, iterations)

    def secant(self, second_guess: float, error_flag: bool = True) -> Tuple[float, int]:
        """
        Secant method: derivative-free method using the two most recent approximations.
        x_{n+1} = x_n - f(x_n)*(x_n - x_{n-1})/(f(x_n) - f(x_{n-1}))
        """
        # intialize with two guesses x_0, x_1
        x_prev = self.initial_guess
        x_current = second_guess

        #iteration counter
        iterations = 0
        
        #termination rule
        while iterations < self.max_iterations:
            #f(x_{n-1}) = f_prev
            f_prev = self.f(x_prev)

            #f(x_n) = f_current
            f_current = self.f(x_current)

            #(f(x_n) - f(x_{n-1}))
            denominator = f_current - f_prev

            if denominator == 0: #division by 0 
                return (x_current, error_flag, iterations)

            #Iteration Scheme: x_{n+1} = x_n - f(x_n)*(x_n - x_{n-1})/(f(x_n) - f(x_{n-1}))
            x_next = x_current - f_current * (x_current - x_prev) / denominator
            iterations += 1
            
            #Sequence converges
            if abs(x_next - x_current) < self. tolerance:
                error_flag = False
                return (x_next, error_flag, iterations)
            
            #Update x_n, x_n-1
            x_prev, x_current = x_current, x_next

        return (x_current, error_flag, iterations)


if __name__ == "__main__":
        # Example function: f(x) = x^2 - 2 (its root is sqrt(2))
    def f(x: float) -> float:
        return x**2 - 2

    def f_prime(x: float) -> float:
        return 2 * x

    initial_guess = 1.0
    tolerance = 1e-7
    max_iterations = 100

    solver = NewtonMethods(f, f_prime, initial_guess, tolerance, max_iterations)

    # Using Newton-Raphson
    nr_root, nr_error, nr_iters = solver.newton_raphson()
    print("Newton-Raphson:")
    print("Approximate root:", nr_root)
    print("Error flag (False means success):", nr_error)
    print("Iterations:", nr_iters)
    print("f(root) =", f(nr_root))

    # Using Lazy Newton (Chord Iteration)
    ln_root, ln_error, ln_iters = solver.lazy_newton()
    print("\nLazy Newton (Chord Iteration):")
    print("Approximate root:", ln_root)
    print("Error flag (False means success):", ln_error)
    print("Iterations:", ln_iters)
    print("f(root) =", f(ln_root))

    # Using Secant Method
    solver_secant = NewtonMethods(f, None, initial_guess, tolerance, max_iterations)
    secant_root, secant_error, secant_iters = solver_secant.secant(1.1)
    print("\nSecant Method:")
    print("Approximate root:", secant_root)
    print("Error flag (False means success):", secant_error)
    print("Iterations:", secant_iters)
    print("f(root) =", f(secant_root))
