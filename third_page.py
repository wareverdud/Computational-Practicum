import matplotlib.pyplot as plt


def run(main):
    n, gte_e, gte_ie, gte_rk = main.run()

    fig, ax = plt.subplots()
    if len(gte_e) != 0:
        ax.plot(n, gte_e, color='blue', linestyle='solid', label='Euler')
    if len(gte_ie) != 0:
        ax.plot(n, gte_ie, color='black', linestyle='solid', label='Improved Euler')
    if len(gte_rk) != 0:
        ax.plot(n, gte_rk, color='red', linestyle='solid', label='Runge-Kutta')
    ax.set_xlabel('N')
    ax.set_ylabel('GTE')
    ax.legend(loc='upper right')
    fig.savefig('figure3.png')
