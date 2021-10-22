from equation import DifferentialEquation


class EulerMethod:
    @staticmethod
    def euler_approx(x, y, h):
        return y + h * DifferentialEquation.f(x, y)
