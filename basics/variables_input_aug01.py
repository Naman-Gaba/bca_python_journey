
marks = int(input("Enter your marks (0 to 100): "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks <= 89:
    print("Grade: B")
elif 60 <= marks <= 74:
    print("Grade: C")
elif 40 <= marks <= 59:
    print("Grade: D")
else:
    print("Grade: F")

