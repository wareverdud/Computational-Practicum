import matplotlib.pyplot as plt


def run(main):
    euler_method_solved, ie_solved, runge_kutta_solved, exact_solved = main.run()
    fig, ax = plt.subplots()
    if len(euler_method_solved) != 0:
        ax.plot(euler_method_solved[0], euler_method_solved[1], color='blue', linestyle='solid', label='Euler')
    if len(ie_solved) != 0:
        ax.plot(ie_solved[0], ie_solved[1], color='black', linestyle='solid', label='Improved Euler')
    if len(runge_kutta_solved) != 0:
        ax.plot(runge_kutta_solved[0], runge_kutta_solved[1], color='red', linestyle='solid', label='Runge-Kutta')
    if len(exact_solved) != 0:
        ax.plot(exact_solved[0], exact_solved[1], color='purple', linestyle='solid', label='Exact')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend(loc='upper right')
    fig.savefig('figure1.png')
