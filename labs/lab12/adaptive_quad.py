# get lgwts routine and numpy
import numpy as np
from gauss_legendre import *
import np.polynomial.legendre as lgwt

# adaptive quad subroutines
# the following three can be passed
# as the method parameter to the main adaptive_quad() function

def eval_composite_trap(M,a,b,f):

  # define h and other sums
  h = (b - a) / M
  xnode = a + np.arange(0, M + 1) * h
  sum = f(a) + f(b)

  # perform trapezoid
  for i in range(1, M):
      x = a + i * h
      sum += 2 * f(x)

  approx = sum * h / 2
  return (approx, xnode, None)

def eval_composite_simpsons(M,a,b,f):
  # define h and other sums
  h = (b - a) / M
  xnode = a + np.arange(0, M + 1) * h
  sum = f(a) + f(b)

  # perform composite simpsons summation
  for i in range(1, M):
      x = a + i * h
      if i % 2 == 0:
          sum += 2 * f(x)
      else:
          sum += 4 * f(x)

  # return as given by composite formula
  return sum * h / 3, xnode, None

def eval_gauss_quad(M, a, b, f):
  """
  Non-adaptive numerical integrator for \int_a^b f(x)w(x)dx
  Input:
    M - number of quadrature nodes
    a,b - interval [a,b]
    f - function to integrate

  Output:
    I_hat - approx integral
    x - quadrature nodes
    w - quadrature weights

  Currently uses Gauss-Legendre rule
  """
  x, w = lgwt.legauss(M, a, b)
  I_hat = np.sum(f(x) * w)
  return I_hat, x, w





