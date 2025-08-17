# Take input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Outer loop for rows
for i in range(rows):
    # Inner loop for columns
    for j in range(cols):
        # Print star if it's first row, last row, first column, or last column
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to next line