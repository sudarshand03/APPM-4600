from typing import Callable, Tuple

class NewtonMethod:
    def __init__(self,
                 func: Callable[[float], float],
                 initial_guess: float,
                 tolerance: float,
                 max_iterations: int,
                 derivative: Callable[[float], float] = None) -> None:
        """
        Initialize the Newton's method solver (single variable)

        :param func: The function f(x) whose root we want to find.
        :param initial_guess: The starting value x0.
        :param tolerance: The convergence tolerance.
        :param max_iterations: Maximum number of iterations allowed.
        :param derivative: (Optional) The analytical derivative f'(x) of f.
                           If not provided, the derivative will be computed numerically.
        """
        self.f: Callable[[float], float] = func
        self.initial_guess: float = initial_guess
        self.tolerance: float = tolerance
        self.max_iterations: int = max_iterations
        self.f_prime: Callable[[float], float] = derivative  # May be None

    