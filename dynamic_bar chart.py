import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Initial data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    new_values = [random.randint(5, 30) for _ in categories]
    ax.bar(categories, new_values, color='orange')
    ax.set_ylim(0, 35)
    ax.set_title('Dynamic Bar Chart (Updating Data)')

ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()
