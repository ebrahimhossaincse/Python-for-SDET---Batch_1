# Define a list of programming languages
languages = ["Python", "Java", "Javascript", "Go", "C", "C++"]

# Index access
print(languages[2])   # Access element at index 2
print(languages[-2])  # Access second-to-last element

# Data slicing
print(languages[2:6])  # Slice from index 2 to 5 (end-1)
print(languages[2:])   # Slice from index 2 to end
print(languages[:5])   # Slice from start to index 4

# Create new list from slice
new_list = languages[:5]
print(new_list)

# Check if element exists in list
if "Go" in languages:
    print("Yes")
else:
    print("No")