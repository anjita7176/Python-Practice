import numpy as np

# Marks of 10 students
marks = np.array([78,65,89,92,56,74,81,69,95,88])

print("Marks of students:", marks)

print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("total marks:", np.sum(marks))

print("Students scored above 80 marks:", np.sum(marks > 80))
print("Students scored below 60 marks:", np.sum(marks < 60))