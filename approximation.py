import exceptions
from solution import ExactSolution


class Approximation:
    @staticmethod
    def solve(x0, y0, X, N, method_of_approximation, c):
        h = (X - x0) / N
        if h >= 1:
            raise exceptions.StepException
        x = [0 for _ in range(N + 1)]
        x[0] = x0
        y = [0 for _ in range(N + 1)]
        y[0] = y0

        y_exact = [0 for _ in range(N + 1)]
        y_exact[0] = y0
        y_with_exact = [0 for _ in range(N + 1)]
        y_with_exact[0] = y0
        lte = [0 for _ in range(N + 1)]
        lte[0] = 0

        for i in range(1, N + 1):
            x[i] = x[i - 1] + h
            y[i] = method_of_approximation(x[i - 1], y[i - 1], h)
            y_exact[i] = ExactSolution.f(x[i], c)
            y_with_exact[i] = method_of_approximation(x[i - 1], y_exact[i - 1], h)
            lte[i] = abs(y_exact[i] - y_with_exact[i])
        return x, y, y_exact, lte
