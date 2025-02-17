import numpy as np
from types import Callable, Tuple


class Bisection:
    def __init__(self,
                 func: Callable[[float], float],
                 lower: float,
                 upper: float,
                 tolerance: float,
                 max_iter: int) -> None:
        """
        param func: input function to find the root
        param lower: the lower bound of interval f(a)
        param upper: upper bound of interval f(b)
        param tolerance: max error bound for convergence
        """

        self.f: Callable[[float], float] = func
        self.lower: float = lower
        self.upper: float = upper
        self.tolerance: float = tolerance
        self.max_iter: int = max_iter

    def solve(self) -> Tuple[float, bool, int]:
        """
        Perform the bisection method

        :return A tuple contiaing:
            - Root
            - error flag (False for Success, True for Error)
            - number of iterations

        :raise Value Error, if IVT doesn't hold
        """

        # how many does the inner loop run
        current_iter = 0

        # endpoints
        lower = self.lower
        upper = self.upper

        # Maximum iterations
        max_iter = self.max_iter

        # error bound
        tol = self.tolerance

        # evaluate the function at the endpoints
        f_lower = self.f(lower)
        f_upper = self.f(upper)

        # Check if IVT holds
        if f_lower * f_upper > 0:
            raise ValueError(
                " The function must change sign on the interval [lower, upper]")

        # Check if the endpoints are exactly the root
        if abs(f_lower) < tol:
            return (self.lower, False, current_iter)
        elif abs(f_upper) < tol:
            return (self.upper, False, current_iter)

        while current_iter < max_iter:

            # midpoint formula that reduces error when (b-a is near max precision)
            # (a + b)/2 might be out of the interval
            midpoint = lower + (upper - lower)/2

            # calculate midpoint
            f_mid = self.f(midpoint)

            # update iterations
            current_iter += 1

            # Check for convergence
            if abs(f_mid) < tol or (upper - lower)/2 < tol:
                return (midpoint, False, current_iter)

            # update endpoints, if a*p > 0 -> roots in [p, b]
            if f_lower * f_mid > 0:
                lower, f_lower = midpoint, f_mid
            else:
                # if a * p < 0 -> roots in [a, p]
                upper = midpoint

        # bisection failed max iterations reached without convergence
        return (midpoint, True, current_iter)

    def error_bound(self, iterations: int) -> float:
        """
        Compute the max error bound of the bisection 
        :param iterations: The number of iterations of the method
        :return: error bound (b-a) / (2^n) (n = number of iterations)
        Bisection converges in O(1/2^n)
        """
        return (self.upper - self.lower)/(2 ** iterations)


if __name__ == "__main__":
    #Example usage
    func = lambda x: 2 * x - 1 - np.sin(x)
    lower = 0.0
    upper = 1.0
    tolerance = 1e-7
    max_iter = 100

    bisector = Bisection(func, lower, upper, tolerance, max_iter)
    approx_root, error_flag, iterations = bisector.solve()
    bound = bisector.error_bound(iterations)

    print("Approximate root:", approx_root)
    print("Error flag (False means success):", error_flag)
    print("Number of iterations:", iterations)
    print("f(root) =", func(approx_root))
    print("Error bound after", iterations, "iterations:", bound)