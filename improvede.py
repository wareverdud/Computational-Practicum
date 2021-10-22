from equation import DifferentialEquation


class ImprovedEulerMethod:
    @staticmethod
    def ie_approx(x, y, h):
        return y + h * DifferentialEquation.f(x + h/2, y + h/2 * DifferentialEquation.f(x, y))
