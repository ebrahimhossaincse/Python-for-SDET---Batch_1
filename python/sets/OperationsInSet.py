# Define two sets with integer elements
set_1 = {1, 2, 3}  # First set
set_2 = {3, 4, 5, 2}  # Second set

# Perform union of set_1 and set_2 (all unique elements from both sets)
union_set = set_1.union(set_2)
print(f"Union: {union_set}")  # Output: Union: {1, 2, 3, 4, 5}

# Perform intersection of set_1 and set_2 (elements common to both sets)
intersection_set = set_1.intersection(set_2)
print(f"Intersection: {intersection_set}")  # Output: Intersection: {2, 3}

# Perform difference of set_1 from set_2 (elements in set_1 but not in set_2)
difference_set = set_1.difference(set_2)
print(f"Difference: {difference_set}")  # Output: Difference: {1}

# Create a copy of set_1
copied_set = set_1.copy()
print(f"Copied Set: {copied_set}")  # Output: Copied Set: {1, 2, 3}