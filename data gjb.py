import numpy as np
import matplotlib.pyplot as plt

def FreeFall(t):
    x0 = 0   # initial position
    v0 = 0   # initial velocity (zero for free fall)
    g = 9.8  # acceleration due to gravity

    # Position for free fall: x(t) = x0 + v0 * t + (1/2) * g * t^2
    x = x0 + v0 * t + 0.5 * g * t**2

    # Velocity for free fall: v(t) = v0 + g * t
    v = v0 + g * t

    data = f"{t}; {round(x, 2)}; {round(v, 2)}\n"

    print(data)

    with open("data_free_fall.txt", "a") as file:
        file.write(data)

    '''
    # Uncomment the following section if you want to plot the position-time and velocity-time graphs
    t_values = np.arange(0.0, T, 0.01)
    x_values = x0 + v0 * t_values + 0.5 * g * t_values**2
    v_values = v0 + g * t_values

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Position (m)', color=color)
    ax1.plot(t_values, x_values, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Velocity (m/s)', color=color)
    ax2.plot(t_values, v_values, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Position and Velocity vs Time for Free Fall')
    plt.show()
    '''

print('t , x , v')
with open("data_free_fall.txt", "w") as file:
    file.write("t; Position; Velocity\n")

for i in range(0, 101):
    t = 0.1 * i
    FreeFall(round(t, 2))
