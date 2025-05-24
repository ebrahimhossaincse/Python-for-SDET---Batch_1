# Function to add two numbers
def add(a, b):
    return a + b

# Call add function and print result
res = add(100, 120)
print(res)

# Function to find maximum number in a list
def find_max(numbers):
    max_num = numbers[0]  # Initialize with first number
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test find_max function with different lists
print("Find Max Number: ", find_max([10, 2, 30, 4, 55, 26, 28.45]))
print("Find Max Number: ", find_max([10, 2, 60, 4, 55, 26, 28.45]))
print("Find Max Number: ", find_max([100, 2, 60, 4, 55, 26, 28, 450]))