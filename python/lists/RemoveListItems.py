# Define the list of programming languages
actual_list = ["Python", "Java", "Javascript", "Go", "C", "C++"]

# Remove specific item by value
actual_list.remove("Go")
print(actual_list)

# Remove item at specific index (index 1)
actual_list.pop(1)
print(actual_list)

# Remove last item
actual_list.pop()
print(actual_list)

# Delete item at specific index (index 1)
del actual_list[1]
print(actual_list)

# Clear all items from the list
actual_list.clear()
print(actual_list)