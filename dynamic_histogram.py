import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

values = []

n = int(input("Enter number of values: "))

for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    values.append(val)

values = np.array(values)

fig, ax = plt.subplots()
bins = np.linspace(min(values), max(values), 10)

def update(frame):
    ax.clear()
    ax.hist(values[:frame+1], bins=bins, edgecolor='black')
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    ax.set_title("Dynamic Histogram (User Input)")

ani = FuncAnimation(fig, update, frames=len(values), interval=500)
plt.show()
