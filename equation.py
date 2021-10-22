import exceptions


class DifferentialEquation:
    @staticmethod
    def f(x, y):
        if x == 0:
            raise exceptions.DerivativeException
        return -y * y / 3 - 2 / (3 * x * x)
