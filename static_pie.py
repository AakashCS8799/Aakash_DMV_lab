import matplotlib.pyplot as plt

# Data
subjects = ['Math', 'Science', 'English', 'History']
marks = [85, 90, 75, 80]

# Create pie chart
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)

# Title
plt.title('Student Marks Distribution')

# Display as circle
plt.axis('equal')

# Show chart
plt.show()
