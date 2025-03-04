import numpy as np
import matplotlib.pyplot as plt
from typing import Callable


class LinearSplineEvaluator:
    def __init__(self, interval_start: float, interval_end: float, function: Callable[[float], float], num_intervals: int):
        """
        Initializes the linear spline evaluator.

        Parameters:
        - interval_start: float -> Start of the interval
        - interval_end: float -> End of the interval
        - function: Callable[[float], float] -> Function to approximate
        - num_intervals: int -> Number of subintervals for the spline
        """
        self.interval_start = interval_start
        self.interval_end = interval_end
        self.function = function
        self.num_intervals = num_intervals
        self.x_intervals = np.linspace(
            interval_start, interval_end, num_intervals + 1)

    def evaluate(self, x_eval: np.ndarray) -> np.ndarray:
        """
        Evaluates a piecewise linear spline approximation at given evaluation points.

        Parameters:
        - x_eval: np.ndarray -> Points where the spline should be evaluated

        Returns:
        - np.ndarray -> Evaluated values of the linear spline at x_eval points
        """
        y_eval = np.zeros_like(x_eval)

        for i in range(self.num_intervals - 1):
            # Define current interval endpoints
            x_left, x_right = self.x_intervals[i], self.x_intervals[i + 1]
            f_left, f_right = self.function(x_left), self.function(x_right)

            # Find indices of x_eval within this interval
            indices = np.where((x_eval >= x_left) & (x_eval <= x_right))[0]

            for idx in indices:
                # Evaluate the linear interpolation at x_eval[idx]
                y_eval[idx] = self.line_evaluator(
                    x_left, f_left, x_right, f_right, x_eval[idx])

        return y_eval

    @staticmethod
    def line_evaluator(a1: float, fa1: float, b1: float, fb1: float, xk: float) -> float:
        """
        Computes linear interpolation at a given point.

        Parameters:
        - a1, b1: float -> Interval points
        - fa1, fb1: float -> Function values at the interval points
        - xk: float -> The point where interpolation is evaluated

        Returns:
        - float -> Interpolated function value at xk
        """
        l0 = (xk - b1) / (a1 - b1)
        l1 = (xk - a1) / (b1 - a1)
        return (fa1 * l0) + (fb1 * l1)


if __name__ == "main":
    pass