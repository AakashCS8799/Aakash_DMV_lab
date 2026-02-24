import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create figure and axis
fig, ax = plt.subplots()

x_data = []
y_data = []

line, = ax.plot([], [], color='blue')

ax.set_xlim(0, 20)
ax.set_ylim(0, 100)
ax.set_title("Animated Line Chart")
ax.set_xlabel("Time")
ax.set_ylabel("Value")

def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 100))
    
    line.set_data(x_data, y_data)
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=20, interval=500)

plt.show()
