# Define a mixed-type list
my_list = [1, 2, 3, "Apple", "Orange", 4.5]

# Using append to add single elements
my_list.append("Banana")  # Add string
my_list.append(True)      # Add boolean
my_list.append(50)        # Add integer
print(my_list)

# Using insert to add elements at specific indices
my_list.insert(3, "Mango")  # Insert string at index 3
print(my_list)
my_list.insert(3, "Test")   # Insert string at index 3
print(my_list)

# Using extend to add multiple elements
my_list.extend(["Pineapple", "Grapes"])  # Add multiple strings
my_list.extend([100, 200])               # Add multiple integers
print(my_list)