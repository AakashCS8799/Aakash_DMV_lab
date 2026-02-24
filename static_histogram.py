import matplotlib.pyplot as plt
import numpy as np

# Static data
data = np.array([15, 20, 25, 30, 35, 40])

# Plot histogram
plt.hist(data, bins=5, color='purple', edgecolor='black')

# Labels and title
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Basic Histogram")

# Display
plt.show()
