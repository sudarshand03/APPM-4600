import numpy as np

def fixedpt(f, x0, tol, Nmax):
    count = 0
    iterations = np.zeros((Nmax + 1, 1))
    iterations[0, 0] = x0

    while count < Nmax:
        count += 1
        x1 = f(x0)
        iterations[count, 0] = x1
        if abs(x1 - x0) < tol:
            ier = 0
            return x1, ier, count, iterations[: count + 1]
        x0 = x1

    ier = 1
    return x1, ier, count, iterations


def convergence(p_true, p_vector):
    numerator = abs(p_vector[-1, 0] - p_true)
    denominator = abs(p_vector[-2, 0] - p_true)
    alpha = 1
    limit = numerator / (denominator ** alpha)

    while limit < 1e-4:
        alpha += 1
        limit = numerator / (denominator ** alpha)

    return alpha, limit


def aitken(p_vector, tol):
    n = p_vector.shape[0]
    aitken_list = []
    ier = 1 
    for k in range(n - 2):
        pn = p_vector[k, 0]
        pn1 = p_vector[k + 1, 0]
        pn2 = p_vector[k + 2, 0]
        denominator = pn2 - 2 * pn1 + pn
        if denominator == 0:
            break 
        pn_hat = pn - ((pn1 - pn) ** 2) / denominator
        aitken_list.append(pn_hat)
        if k > 0 and abs(aitken_list[-1] - aitken_list[-2]) < tol:
            ier = 0
            return pn_hat, np.array(aitken_list).reshape(-1, 1), ier, k + 1

    return pn_hat, np.array(aitken_list).reshape(-1, 1), ier, len(aitken_list)


def steffenson(f, x0, tol, Nmax):
    count = 0
    iterations = np.zeros((Nmax + 1, 1))
    iterations[0, 0] = x0

    while count < Nmax - 2:
        a = x0
        count += 1
        b = f(x0)
        iterations[count, 0] = b
        if abs(a - b) < tol:
            ier = 0
            return b, ier, count, iterations[: count + 1]

        count += 1
        c = f(b)
        iterations[count, 0] = c
        if abs(b - c) < tol:
            ier = 0
            return c, ier, count, iterations[: count + 1]

        denominator = c - 2 * b + a
        if denominator == 0:
            ier = 1
            return x0, ier, count, iterations[: count + 1]
        count += 1
        x0 = a - ((b - a) ** 2) / denominator
        iterations[count, 0] = x0
        if abs(b - c) < tol:
            ier = 0
            return x0, ier, count, iterations[: count + 1]

    ier = 1
    return x0, ier, count, iterations[: count + 1]


if __name__ == "__main__":

    g = lambda x: np.sqrt(10 / (x + 4))

    Nmax = 100
    tol = 1e-10
    x0 = 1.5
    p_true = 1.3652300134140976 

    xstar, ier, count, iterations = fixedpt(g, x0, tol, Nmax)
    print("FIXED POINT")
    print("The number of iterations was:", count)
    print("The approximate fixed point is:", xstar)
    if ier == 0:
        order, constant = convergence(p_true, iterations)
        print("The convergence is of order:", order)
        print("With asymptotic error constant:", constant)
        print("Iterations:\n", iterations)
    else:
        print("The sequence did not converge")
    print("Error message reads:", ier)

    xstar, aitken_iters, ier, count = aitken(iterations, tol)
    print("\nAITKEN'S")
    print("The number of iterations was:", count)
    print("The approximate fixed point is:", xstar)
    if ier == 0:
        order, constant = convergence(p_true, aitken_iters)
        print("The convergence is of order:", order)
        print("With asymptotic error constant:", constant)
        print("Iterations:\n", aitken_iters)
    else:
        print("The sequence did not converge")
    print("Error message reads:", ier)

    xstar, ier, count, iterations = steffenson(g, x0, tol, Nmax)
    print("\nSTEFFENSEN'S")
    print("The number of iterations was:", count)
    print("The approximate fixed point is:", xstar)
    if ier == 0:
        order, constant = convergence(p_true, iterations)
        print("The convergence is of order:", order)
        print("With asymptotic error constant:", constant)
        print("Iterations:\n", iterations)
    else:
        print("The sequence did not converge")
    print("Error message reads:", ier)
