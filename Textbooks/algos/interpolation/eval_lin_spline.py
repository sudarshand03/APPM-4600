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

        # Define the function f(x)
    def f(x):
        return 1 / (1 + (10 * x) ** 2)


    # Define the number of interpolation points
    N = 10  # Number of nodes (you can change this)
    h = 2 / (N - 1)

    # Generate interpolation nodes
    x_nodes = np.array([-1 + (j - 1) * h for j in range(N)])
    y_nodes = f(x_nodes)

    # Generate evaluation points
    x_eval = np.linspace(-1, 1, 200)

    # Use the LinearSplineEvaluator class from previous implementation
    evaluator = LinearSplineEvaluator(
        interval_start=-1, interval_end=1, function=f, num_intervals=N-1)
    y_eval = evaluator.evaluate(x_eval)

    # Plot the function and the linear spline interpolation
    plt.figure(figsize=(8, 5))
    plt.plot(x_eval, f(x_eval), label="True Function $f(x)$",
            linestyle="dashed", color="black")
    plt.plot(x_eval, y_eval, label="Linear Spline Approximation", color="red")
    plt.scatter(x_nodes, y_nodes, color="blue",
                label="Interpolation Nodes", zorder=3)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Linear Spline Interpolation of $f(x) = \\frac{1}{1 + (10x)^2}$")
    plt.legend()
    plt.grid()
    plt.show()
