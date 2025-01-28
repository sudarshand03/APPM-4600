# Quesiton 1

Evaluate $f(x)=x^2(x-1)$ using the bisection method with intervals

*a* (0.5,2)

the approximate root is 0.9999999701976776

the error message reads: 0

f(astar) = -2.98023206113385e-08

*b* (-1,0.5)

the approximate root is -1

the error message reads: 1

f(astar) = -2

*c* (-1,2)

the approximate root is 0.9999999701976776

the error message reads: 0

f(astar) = -2.98023206113385e-08


Yes the bisection method worked as expected, it found the roots where they existed in the interval and errored where it didn't. The bisection method cannot find the root x=0 since it has even multiplicity so f(x) does not change sign at x=0 and the IVT doesn't apply.


# Question 2
Apply Bisection to the following functions with tolerance $\epsilon =10^{-5}$

*a)* $f(x)=(x-1)(x-3)(x-5)$ with $(a,b)=(0,2.4)$

the approximate root is 1.0000030517578122

the error message reads: 0

*b)* f(astar) = 2.4414006618542327e-05


*c)* $f(x)=(x-1)^2(x-3)$ with $(a,b)=(0,2)$

the approximate root is 0

the error message reads: 1

f(astar) = -3

*d)* $f(x)=\sin(x)$ with $(a,b)=(0,0.1)$

the approximate root is 0

the error message reads: 0

f(astar) = 0.0



*e)* $f(x)=\sin(x)$ and $(a,b)=(0.5, \frac{3\pi}{4})$

the approximate root is 0.5

the error message reads: 1

f(astar) = 0.479425538604203


*Is the behavior what you expect? Was your code successful? Did it achieve at least the desired
accuracy?* 

Yes this is the behavior expected from each of the functions, whenever the hypothesis of the IVT were achived the bisection method successfully found the roots of the functions with error bound $\epsilon=10^{-5}$

# Question 3

$f(x)=x(1+ \frac{7-x^5}{x^2})^3$

Fixed point iteration failed to converge due to overflow error


$f(x)=x-\frac{x^5-7}{x^2}$

Fixed point iteration failed to converge due to overflow error


$f(x)=x-\frac{x^5-7}{5x^4}$

the approximate fixed point is: 1.475773161594552

f1(xstar): 1.4757731615945522

Error message reads: 0

$f(x)=x-\frac{x^5-7}{12}$
the approximate fixed point is: 1.473578045466708

f1(xstar): 1.4779035096682074

Error message reads: 0


For which functions does the fixed point iteration converge? For which functions does it not converge? Try
to come up with an explanation of why the fixed point iteration performs the way it does
for each of the functions


 *(a):* Does not converge due to large derivative magnitude around $x^*$.

 *(b):* Does not converge due to $|f'(x)| \approx 1 $
 
 *(c):* Converges fast because $f'(x^*) = 0$

 *(d):* Converges slowly because $|f'(x)| < 1$  but close to 1