# ----------------------------
# Tuple Operations in Python
# ----------------------------

# Copy
original_tuple = (1, 6, 3, 9, 5, 4, 2)
original_tuple2 = (11, 6, 23, 9, 55, 4, 2)

# Copying a tuple (simple assignment creates a reference to the original)
copied_tuple = original_tuple
print(f"Copied Tuple: {copied_tuple}")

# Sort
# 'sorted' returns a sorted list, not a tuple
sorted_tuple = tuple(sorted(original_tuple))
print(f"Sorted Tuple: {sorted_tuple}")

# Join
# Concatenating two tuples
joined_tuple = original_tuple + original_tuple2
print(f"Joined Tuple: {joined_tuple}")

# Nested Tuple
# Creating a tuple containing other tuples (i.e., a 2D tuple)
nested_tuple = ((1, 2, 3), (4, 5, 6, 9, 8))
print(f"Nested Tuple: {nested_tuple}")

# Accessing elements in a nested tuple
print(f"Second element of first inner tuple: {nested_tuple[0][1]}")
print(f"Fourth element of second inner tuple: {nested_tuple[1][3]}")
