import matplotlib.pyplot as plt

# Data
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 20, 25]

# Create pie chart
plt.figure()
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

# Equal aspect ratio ensures pie is circular
plt.axis('equal')

plt.title("Fruit Distribution Pie Chart")

plt.show()
