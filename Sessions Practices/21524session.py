# Take the length of rectangle from the user
length = float(input("Enter the length of the rectangle: "))

# Take the width of rectangle from the user
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = length * width

# Display the area
print("The area of the rectangle is:", area)

# Increase the width of rectangle by 0.5
new_width = width + 0.5

# Recalculate the area in new variable
new_area = length * new_width

# Display the old area and new area
print("Old area:", area)
print("New area:", new_area)