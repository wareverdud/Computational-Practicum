import exceptions
from numpy import cbrt


class ExactSolution:
    @staticmethod
    def f(x, c):
        if x == 0 or float(cbrt(x)) == -c:
            raise exceptions.SolutionException()
        return (c + 2 * float(cbrt(x))) / (c*x + x*float(cbrt(x)))

    @staticmethod
    def solve(x0, X, N, c):
        if x0 <= (-(c ** 3)) <= X or X <= (-(c ** 3)) <= x0:
            raise exceptions.SolutionException()
        if x0 <= 0 <= X or X <= 0 <= x0:
            raise exceptions.SolutionException()
        h = (X - x0) / N
        if h >= 1:
            raise exceptions.StepException
        x = [0 for _ in range(N + 1)]
        y = [0 for _ in range(N + 1)]
        x[0] = x0
        y[0] = ExactSolution.f(x[0], c)
        for i in range(1, N+1):
            x[i] = x[i-1] + h
            y[i] = ExactSolution.f(x[i], c)
        return x, y
