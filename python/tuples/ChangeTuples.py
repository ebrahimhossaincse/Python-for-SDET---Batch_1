# Define a tuple with mixed data types
my_tuple = (1, 2, "username", "password")  # Contains integers and strings

# Create a new tuple by concatenating a slice of my_tuple with a new single-element tuple
new_tuple = my_tuple[:3] + ("python",)  # Slice up to index 3 and add "python"
print(f"New Tuple: {new_tuple}")  # Output: New Tuple: (1, 2, 'username', 'python')

# Print the existing tuple to show it remains unchanged
print(f"Existing Tuple: {my_tuple}")  # Output: Existing Tuple: (1, 2, 'username', 'password')

# Delete the entire tuple
del my_tuple
# Attempt to print the deleted tuple (will raise an error)
print(f"Deleted Tuple: {my_tuple}")  # Raises NameError: name 'my_tuple' is not defined