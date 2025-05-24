# Define a dictionary with personal information
my_dict = {
    "Name": "Ebrahim",          # Person's name
    "Company": "Academy",       # Company name
    "University": "DIU",        # University name
    "Phone": "01886644261",    # Phone number
    "Batch": 43                # Batch number
}

# Remove and return the value for the specified key using pop()
my_dict.pop("University")      # Removes the 'University' key-value pair
print(my_dict)                 # Output: {'Name': 'Ebrahim', 'Company': 'Academy', 'Phone': '01886644261', 'Batch': 43}

# Remove and return the last inserted key-value pair using popitem()
my_dict.popitem()              # Removes the last inserted item ('Batch': 43)
print(my_dict)                 # Output: {'Name': 'Ebrahim', 'Company': 'Academy', 'Phone': '01886644261'}

# Delete a specific key-value pair using del
del my_dict["Company"]         # Removes the 'Company' key-value pair
print(my_dict)                 # Output: {'Name': 'Ebrahim', 'Phone': '01886644261'}

# Remove all items from the dictionary using clear()
my_dict.clear()                # Empties the dictionary
print(my_dict)                 # Output: {}