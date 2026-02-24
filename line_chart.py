import numpy as np
import matplotlib.pyplot as plt

x_axis = np.array([10, 20, 30, 40, 50])
y_axis = np.array([5, 15, 25, 35, 45])

plt.figure(figsize=(8, 5))
plt.plot(x_axis, y_axis, marker='o')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Chart")

plt.show()
