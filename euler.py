from equation import DifferentialEquation as de


class EulerMethod:
    @staticmethod
    def euler_approx(x, y, h):
        return y + h * de.f(x, y)
