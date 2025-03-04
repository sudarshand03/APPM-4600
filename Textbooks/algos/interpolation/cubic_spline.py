import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from typing import Callable


class CubicSplineInterpolator:
    def __init__(self, function: Callable[[float], float], start: float, end: float, num_intervals: int):
        self.function = function
        self.start = start
        self.end = end
        self.num_intervals = num_intervals
        self.step_size = (end - start) / num_intervals
        self.nodes = np.linspace(start, end, num_intervals + 1)
        self.function_values = np.array([function(x) for x in self.nodes])
        self.second_derivatives = self._compute_second_derivatives()

    def evaluate(self, evaluation_points: np.ndarray) -> np.ndarray:
        spline_values = np.zeros_like(evaluation_points)

        for i in range(self.num_intervals - 1):
            x_left, x_right = self.nodes[i], self.nodes[i + 1]
            indices = np.where((evaluation_points >= x_left)
                               & (evaluation_points <= x_right))[0]
            for idx in indices:
                spline_values[idx] = self._evaluate_spline_segment(
                    x_left, self.function_values[i], x_right, self.function_values[i + 1],
                    self.second_derivatives[i], self.second_derivatives[i +
                                                                        1], evaluation_points[idx]
                )
        return spline_values

    def _compute_second_derivatives(self) -> np.ndarray:
        num_nodes = self.num_intervals + 1
        coefficient_matrix = np.zeros((num_nodes - 2, num_nodes - 2))
        coefficient_matrix[0, 0], coefficient_matrix[0, 1] = 1 / 3, 1 / 12

        for i in range(1, num_nodes - 3):
            coefficient_matrix[i, i - 1], coefficient_matrix[i,
                                                             i], coefficient_matrix[i, i + 1] = 1 / 12, 1 / 3, 1 / 12

        coefficient_matrix[num_nodes - 3, num_nodes -
                           4], coefficient_matrix[num_nodes - 3, num_nodes - 3] = 1 / 12, 1 / 3

        rhs_vector = np.array([
            (self.function_values[i + 2] - 2 * self.function_values[i + 1] + self.function_values[i]) /
            (2 * self.step_size**2) for i in range(num_nodes - 2)
        ])
        second_derivatives = np.insert(
            inv(coefficient_matrix) @ rhs_vector, [0, len(rhs_vector)], 0)
        return second_derivatives

    @staticmethod
    def _evaluate_spline_segment(
        x_left: float, f_left: float, x_right: float, f_right: float,
        second_derivative_left: float, second_derivative_right: float, x_eval: float
    ) -> float:
        step_size = x_right - x_left
        linear_term_left = (f_left / step_size) - \
            (step_size * second_derivative_left / 6)
        linear_term_right = (f_right / step_size) - \
            (step_size * second_derivative_right / 6)
        return (
            (((x_right - x_eval) ** 3 * second_derivative_left) / (6 * step_size)) +
            (((x_eval - x_left) ** 3 * second_derivative_right) / (6 * step_size)) +
            (linear_term_left * (x_right - x_eval)) +
            (linear_term_right * (x_eval - x_left))
        )


if __name__ == "main":
    pass