# Define a set with mixed data types
my_set = {1, 2, 3, 4, 5, 6, 'Java', 'Python', 'Go', 'Javascript'}  # Contains integers and strings

# Remove a specific element using remove()
my_set.remove("Go")  # Removes "Go" from the set; raises KeyError if not found
print(f"my_set: {my_set}")  # Print set after removing "Go"

# Remove a specific element using discard()
my_set.discard(4)  # Removes 4 from the set; does nothing if not found
print(f"my_set: {my_set}")  # Print set after discarding 4

# Remove and return an arbitrary element using pop()
my_set.pop()  # Removes a random element (sets are unordered)
print(f"my_set: {my_set}")  # Print set after popping an element

# Remove all elements from the set using clear()
my_set.clear()  # Empties the set
print(f"my_set: {my_set}")  # Print the empty set