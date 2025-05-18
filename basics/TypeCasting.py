# Type Casting -> result = dataType(Variable)

# Float to Integer
height = 5.000000231
print(type(height))  # Output: <class 'float'>
res = int(height)
print(res)  # Output: 5
print("Type of res is:", type(res))  # Output: <class 'int'>

# String to Float
sum = "100.50"
sum_num = float(sum)
print(sum_num)  # Output: 100.5
print("Type of sum_num is:", type(sum_num))  # Output: <class 'float'>