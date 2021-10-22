import exceptions


class DifferentialEquation:
    @staticmethod
    def f(x, y):
        # Equation 10
        if x == 0:
            raise exceptions.Derivative
        return -y * y / 3 - 2 / (3 * x * x)
        # Equation 6
        # return 2*x*(x*x + y)
