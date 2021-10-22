from equation import DifferentialEquation


class RungeKuttaMethod:
    @staticmethod
    def runge_kutta_approx(x, y, h):
        k1 = DifferentialEquation.f(x, y)
        k2 = DifferentialEquation.f(x + h/2, y + h * k1 / 2)
        k3 = DifferentialEquation.f(x + h/2, y + h * k2 / 2)
        k4 = DifferentialEquation.f(x + h, y + h * k3)
        return y + h * (k1 + 2*k2 + 2*k3 + k4) / 6
