# Section 1: Basic Shorthand Conditional (Commented)
# Get user input
x = int(input("Enter a number: "))
# print("Positive" if x > 0 else "Negative")  # Commented in original

# Section 2: Nested If-Else and Shorthand Equivalent
print("Section 2: Nested If-Else and Shorthand")
if x > 10:
    print("Large")
else:
    if x < 5:
        print("Small")

# Nested shorthand conditional
result = "Large" if x > 10 else "Small" if x < 5 else "Medium"
print(result)