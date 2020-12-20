# from matplotlib import pyplot as plt
import numpy as np
x0 = 22
h = 0.1


def f(x):
    return (2*x+1)/((2/3)-2*x)


def g(x):
    return (np.e**(2*x))-10


x0 = 0
x1 = 0

while abs(f(x0)) > 0.0001:
    x0 -= f(x0)/((f(x0+h)-f(x0))/h)  # Algoritmen beskrevet i Newtons metode.

while abs(g(x1)) > 0.0001:
    x1 -= g(x1)/((g(x1+h)-g(x1))/h)  # Algoritmen beskrevet i Newtons metode.

print(x0)
print(x1)
