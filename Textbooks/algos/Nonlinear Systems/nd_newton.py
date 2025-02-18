import numpy as np
from numpy import ndarray
from numpy.linalg import norm, inv
from typing import Callable, Tuple, Union, List


class system_newton:
    def __init__(
        self,
        system: Callable[[ndarray], ndarray],
        jacobian: Callable[[ndarray], ndarray],
        # list of floats, or an numpy array
        inital_guess: Union[List[float], ndarray],
        tolerance: float = 1e-10,
        max_iter: int = 100
        ) -> None:
        
        self.system: Callable[[ndarray], ndarray] = system
        self.jacobian: Callable[[ndarray], ndarray] = jacobian
        self.tolerance: float = tolerance
        self.max_iter: int = max_iter
        self.intial_guess: Union[List[float], ndarray]

    def newton_raphson(self, error_flag: bool = True
                       ) -> Tuple[ndarray, bool, int]:
        iterations = 0

        # intialize x_0
        x_current = np.array(self.intial_guess)

        # error tolerance
        while iterations < self.max_iter:
            # Evaluate system of equations on current approximation
            eval_f = self.system(x_current)
            # Evaluate Jacobian on current approximation
            eval_jac = self.jacobian(x_current)
            # invert jacboian (used in iteration)
            inv_jac = inv(eval_jac)

            # x_1 = x_0 + y = x_0 - J(x_0)^-1*F(x_0)
            x_next = x_current - inv_jac @ eval_f

            iterations += 1

            if norm(x_next - x_current) < self.tolerance:
                error_flag = False
                return (x_next, error_flag, iterations)

            x_current = x_next

        return (x_current, error_flag, iterations)  # iterations failed

    def lazy_newtons(self, error_flag: bool = True
                     ) -> Tuple[ndarray, bool, int]:

        iterations = 0
        # intialize x_0
        x_current = np.array(self.intial_guess)

        eval_jac = self.jacobian(x_current)
        inv_jac = inv(eval_jac)
        # error tolerance
        while iterations < self.max_iter:
            # Evaluate system of equations on current approximation
            eval_f = self.system(x_current)

            # x_n = x_{n-1} + y = x_{n-1} - J(x_0)^-1*F(x_{n-1})
            # Use precomputed inverse
            x_next = x_current - inv_jac @ eval_f
            iterations += 1

            if norm(x_next - x_current) < self.tolerance:
                error_flag = False
                return (x_next, error_flag, iterations)

            x_current = x_next

        return (x_current, error_flag, iterations)  # iterations failed

    def solve_broyden(self, error_flag: bool = True) -> Tuple[ndarray, bool, int]:
        """
        Broyden's method using the Sherman–Morrison update.

        This method begins with one Newton step to initialize an approximate inverse
        Jacobian, and then iteratively updates this approximation.

        Returns (solution, error_flag, iterations), where error_flag is False if converged.
        """
        # Convert the initial guess to a NumPy array.
        current_x = np.array(self.initial_guess, dtype=float)

        # Initial Newton step to set up the approximate inverse Jacobian.
        initial_jacobian= self.jacobian(current_x)
        F_current  = self.system(current_x)
        approx_inv_jacobian  = inv(initial_jacobian)
        step  = -approx_inv_jacobian.dot(F_current)
        current_x = current_x + step

        # Iterate up to max_iter times.
        for iteration in range(self.max_iter):
            # Save the previous function evaluation.
            F_previous: ndarray = F_current.copy()
            
            F_current = self.system(current_x)
            delta_F: ndarray = F_current - F_previous

            # Compute the adjustment direction for the inverse Jacobian update
            update_direction= -approx_inv_jacobian.dot(delta_F)

            #scaling denominator for the Sherman–Morrison update.
            scaling_denominator = -np.dot(step, update_direction)

            if abs(scaling_denominator) < 1e-12:
                # Breakdown: the update is unstable.
                return (current_x, True, iteration)
            
            # Compute the product of the step with the current inverse Jacobian.
            step_times_inv_jacobian= np.dot(
                step, approx_inv_jacobian)
            
            # Form the update vector for the inverse Jacobian.
            update_vector = step + update_direction

            # Sherman–Morrison formula.
            approx_inv_jacobian = approx_inv_jacobian + \
                (1.0 / scaling_denominator) * \
                np.outer(update_vector, step_times_inv_jacobian)
            
            # Compute the next Newton-like step.
            step = -approx_inv_jacobian.dot(F_current)

            # Update the current iterate.
            current_x = current_x + step

            if norm(step) < self.tolerance:
                error_flag = False
                return (current_x, error_flag, iteration)

        return (current_x, error_flag, self.max_iter)
    


