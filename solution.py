import exceptions
from numpy import cbrt
import numpy as np


class ExactSolution:
    @staticmethod
    def f(x, c):
        # Equation 10
        if x == 0 or cbrt(x) == -c:
            raise exceptions.Solution(x)
        return (c + 2 * cbrt(x)) / (c*x + x*cbrt(x))
        # Equation 6
        # return c*float(np.exp(x*x)) - x*x - 1

    @staticmethod
    def solve(x0, X, N, c):
        h = (X - x0) / N
        if h >= 1:
            raise exceptions.Step
        x = [0 for _ in range(N + 1)]
        x[0] = x0
        y = [0 for _ in range(N + 1)]
        y[0] = ExactSolution.f(x[0], c)
        for i in range(1, N+1):
            x[i] = x[i-1] + h
            y[i] = ExactSolution.f(x[i], c)
        return x, y
