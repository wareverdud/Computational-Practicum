import exceptions
from solution import ExactSolution
from approximation import Approximation
from euler import EulerMethod
from improvede import ImprovedEulerMethod
from rungekutta import RungeKuttaMethod
from numpy import cbrt


class Main:
    def __init__(self):
        self.N = 5
        self.x0 = 1
        self.y0 = 2
        self.X = 5

        self.e = True
        self.ie = True
        self.rk = True
        self.ex = True

    def run(self):
        if self.x0 * self.y0 == 1:
            raise exceptions.ConstantException
        c = (self.x0 * self.y0 - 2) * float(cbrt(self.x0)) / (1 - self.x0 * self.y0)

        euler_method_solved = []
        ie_solved = []
        runge_kutta_solved = []
        exact_solved = []
        if self.e:
            euler_method_solved = Approximation.solve(self.x0, self.y0, self.X, self.N, EulerMethod.euler_approx,
                                                      c)
        if self.ie:
            ie_solved = Approximation.solve(self.x0, self.y0, self.X, self.N, ImprovedEulerMethod.ie_approx, c)
        if self.rk:
            runge_kutta_solved = Approximation.solve(self.x0, self.y0, self.X, self.N,
                                                     RungeKuttaMethod.runge_kutta_approx, c)
        if self.ex:
            exact_solved = ExactSolution.solve(self.x0, self.X, self.N, c)
        return euler_method_solved, ie_solved, runge_kutta_solved, exact_solved


class MainUpdated(Main):
    def __init__(self):
        super().__init__()
        self.n0 = 5
        self.n_final = 19

    def run(self):
        if self.n_final < self.n0:
            raise exceptions.NumberOfStepsException
        n = []
        gte_e = []
        gte_ie = []
        gte_rk = []
        for i in range(self.n0, self.n_final + 1):
            self.N = i
            euler_method_solved, ie_solved, runge_kutta_solved, exact_solved = super().run()
            n.append(i)
            if self.e:
                gte_e.append(max(euler_method_solved[3]))
            if self.ie:
                gte_ie.append(max(ie_solved[3]))
            if self.rk:
                gte_rk.append(max(runge_kutta_solved[3]))
        return n, gte_e, gte_ie, gte_rk
