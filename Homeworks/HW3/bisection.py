import numpy as np
from types import LambdaType


def bisection(func: LambdaType, lower: float, upper: float, tolerance: float) -> list:
    f_lower = func(lower)
    f_upper = func(upper)

    if f_lower * f_upper > 0:
        return [lower, 1, 0]

    if f_lower == 0:
        return [lower, 0, 0]
    if f_upper == 0:
        return [upper, 0, 0]

    iterations = 0

    while (upper - lower) / 2 > tolerance:
        midpoint = (lower + upper) / 2.0
        f_mid = func(midpoint)
        iterations += 1

        if f_mid == 0:
            return [midpoint, 0, iterations]

        if f_lower * f_mid < 0:
            upper, f_upper = midpoint, f_mid
        else:
            lower, f_lower = midpoint, f_mid

    approx_root = (lower + upper) / 2.0
    return [approx_root, 0, iterations]

if __name__ == '__main__':

    # Question 1:
    func = lambda x: 2*x - 1 - np.sin(x)
    lower = 0
    upper = 1
    tolerance = 1e-7

    approx_root, error_flag, iterations = bisection(func, lower, upper, tolerance)


    print("The approximate root is:", approx_root)
    print("The error flag is:", error_flag)
    print("f(root) =", func(approx_root))
    print("Number of iterations:", iterations)


    #Question 2
    # # FACTORED form
    # f_factored = lambda x: (x - 5)**9

    # lower = 4.82
    # upper = 5.2
    # tolerance = 1e-4

    # approx_root_factored, err_factored, iters_factored = bisection(f_factored, lower, upper, tolerance)

    # print("=== Factored (x-5)^9 ===")
    # print("Approx. root:", approx_root_factored)
    # print("f(root) =", f_factored(approx_root_factored))
    # print("Iterations:", iters_factored)
    # print("Error flag:", err_factored)



    #     # EXPANDED polynomial
    # f_expanded = lambda x: (
    #     x**9
    #     - 45*x**8
    #     + 900*x**7
    #     - 10500*x**6
    #     + 78750*x**5
    #     - 390625*x**4
    #     + 1312500*x**3
    #     - 2812500*x**2
    #     + 3515625*x
    #     - 1953125
    # )

    # lower = 4.82
    # upper = 5.2
    # tolerance = 1e-4

    # approx_root_expanded, err_expanded, iters_expanded = bisection(f_expanded, lower, upper, tolerance)

    # print("=== Expanded (x-5)^9 ===")
    # print("Approx. root:", approx_root_expanded)
    # print("f(root) =", f_expanded(approx_root_expanded))
    # print("Iterations:", iters_expanded)
    # print("Error flag:", err_expanded)

    # # Question 3:
    # func = lambda x: x**3 + x - 4
    # lower = 1
    # upper = 4
    # tolerance = 1e-3

    # approx_root, error_flag, iterations = bisection(func, lower, upper, tolerance)


    # print("The approximate root is:", approx_root)
    # print("The error flag is:", error_flag)
    # print("f(root) =", func(approx_root))
    # print("Number of iterations:", iterations)
