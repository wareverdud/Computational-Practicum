from equation import DifferentialEquation as de


class ImprovedEulerMethod:
    @staticmethod
    def ie_approx(x, y, h):
        return y + h * de.f(x + h/2, y + h/2 * de.f(x, y))
