import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [150, 200, 250, 300]

# Create bar chart
plt.bar(months, sales, color='skyblue')

# Labels and title
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Report')

# Show chart
plt.show()
