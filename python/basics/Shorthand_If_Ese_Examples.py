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

# Nested If-Else (Complex Conditions)
print("Section 3: Nested If-Else")
age = 20
citizenship = "BD"
# Regular
if age >= 18:
    if citizenship == "BD":
        result = "Eligible to vote"
    else:
        result = "Ineligible due to citizenship"
else:
    result = "Ineligible due to age"
print(result)  # Output: Eligible to vote
# Shorthand
result = "Eligible to vote" if age >= 18 and citizenship == "BD" else "Ineligible due to citizenship" if age >= 18 else "Ineligible due to age"
print(result)  # Output: Eligible to vote