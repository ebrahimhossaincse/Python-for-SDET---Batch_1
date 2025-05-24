# Define the list of programming languages
actual_list = ["Python", "Java", "Javascript", "Go", "C", "C++"]

# Commented-out: Simple loop to print each element
for x in actual_list:
    print(x)

# Commented-out: Loop using range to print elements
for x in range(len(actual_list)):
    print(actual_list[x])

# Loop using range to print index and value
for i in range(len(actual_list)):
    print(f"Index: {i} Value: {actual_list[i]}")

# List comprehension equivalent of the above loop
[print(f"Index: {i} Value: {actual_list[i]}") for i in range(len(actual_list))]