import matplotlib.pyplot as plt


def run(main):
    euler_method_solved, ie_solved, runge_kutta_solved, exact_solved = main.run()
    fig, ax = plt.subplots()
    if len(euler_method_solved) != 0:
        ax.plot(euler_method_solved[0], euler_method_solved[3], color='blue', linestyle='solid', label='Euler')
    if len(ie_solved) != 0:
        ax.plot(ie_solved[0], ie_solved[3], color='black', linestyle='solid', label='Improved Euler')
    if len(runge_kutta_solved) != 0:
        ax.plot(runge_kutta_solved[0], runge_kutta_solved[3], color='red', linestyle='solid', label='Runge-Kutta')
    ax.set_xlabel('X')
    ax.set_ylabel('LTE')
    ax.legend(loc='upper right')
    fig.savefig('figure2.png')
