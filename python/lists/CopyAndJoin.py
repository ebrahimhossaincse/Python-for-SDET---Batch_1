# Define the original list of programming languages
actual_list = ["Python", "Java", "Javascript", "Go", "C", "C++"]

# Copy the list using copy() method
mylist = actual_list.copy()
print(mylist)

# Copy the list using list() constructor
test_list = list(actual_list)
print(test_list)

# Copy a slice of the list (first four elements)
slice_list = actual_list[:4]
print(slice_list)

# Join two lists using concatenation
list1 = ["Python", "Java"]
list2 = ["Javascript", "Go", "C", "C++"]
list3 = list1 + list2
print(list3)

# Join lists by appending elements
for x in list2:
    list1.append(x)
print(list1)