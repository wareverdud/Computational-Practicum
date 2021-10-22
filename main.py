import exceptions
import solution
from approximation import Approximation
from euler import EulerMethod
from improvede import ImprovedEulerMethod
from rungekutta import RungeKuttaMethod
from numpy import cbrt
import numpy as np


class Main:
    def __init__(self):
        # Equation 10
        self.N = 5  # -> not specified
        self.x0 = 1
        self.y0 = 2
        self.X = 5  # -> 5

        # Equation 6
        # self.N = 5
        # self.x0 = 0
        # self.y0 = 0
        # self.X = 10

        self.e = True
        self.ie = True
        self.rk = True
        self.ex = True
        self.c = 0

    # def set_c(self, ):
    #     c = self.

    def run(self):

        # c = (self.x0 * self.y0 - 2) * self.x0 ** (1 / 3) / (1 - self.x0 * self.y0)

        # Equation 10
        if self.x0 * self.y0 == 1:
            raise exceptions.Constant
        self.c = (self.x0 * self.y0 - 2) * cbrt(self.x0) / (1 - self.x0 * self.y0)

        # Equation 6
        # self.c = (self.x0*self.x0 + self.y0 + 1) / float(np.exp(self.x0*self.x0))

        # self.c = float(self.c)
        # temp1 = self.x0 * self.y0 - 2
        # temp2 = self.x0**(1/3)
        # temp2 = pow(self.x0, 1/3)
        # temp2 = np.cbrt(self.x0)
        # temp3 = 1-self.x0*self.y0
        # tempmul = temp1 * temp2
        # tempfinal = tempmul / temp3

        euler_method_solved = []
        ie_solved = []
        runge_kutta_solved = []
        exact_solved = []
        if self.e:
            euler_method_solved = Approximation.solve(self.x0, self.y0, self.X, self.N, EulerMethod.euler_approx,
                                                      self.c)
            # print('Euler method:')
            # for i in euler_method_solved:
            #     for j in i:
            #         print(f'{float(j):.5f}', end=' ')
            #     print()
        if self.ie:
            ie_solved = Approximation.solve(self.x0, self.y0, self.X, self.N, ImprovedEulerMethod.ie_approx, self.c)
            # print('Improved Euler method:')
            # for i in ie_solved:
            #     for j in i:
            #         print(f'{float(j):.5f}', end=' ')
            #     print()
        if self.rk:
            runge_kutta_solved = Approximation.solve(self.x0, self.y0, self.X, self.N,
                                                     RungeKuttaMethod.runge_kutta_approx, self.c)
            # print('Runge-Kutta method:')
            # for i in runge_kutta_solved:
            #     for j in i:
            #         print(f'{float(j):.5f}', end=' ')
            #     print()
        if self.ex:
            exact_solved = solution.ExactSolution.solve(self.x0, self.X, self.N, self.c)
        return euler_method_solved, ie_solved, runge_kutta_solved, exact_solved


class MainUpdated(Main):
    def __init__(self):
        super().__init__()
        self.n0 = 5
        self.n_final = 19

    def run(self):
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


if __name__ == '__main__':
    # main = Main()
    # main.N = 5
    # main.x0 = -0.5
    # main.X = 1
    # main.run()

    # main1 = Main()
    # main1.N = 10
    # main1.x0 = -0.5
    # main1.X = 0.5
    # main1.run()

    # main2 = MainUpdated()
    # main2.N = 10
    # main2.x0 = -0.5
    # main2.X = 0.5
    # main2.n0 = 1
    # main2.run()
    # derivative exception

    # main3 = Main()
    # main3.N = 2
    # main3.x0 = -0.1
    # main3.X = 0.1
    # main3.run()

    # main4 = Main()
    # main4.N = 35
    # main4.x0 = -2
    # main4.X = 2
    # main4.y0 = 7
    # main4.run()

    main5 = Main()
    main5.run()

