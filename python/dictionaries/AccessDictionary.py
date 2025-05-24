# Define a dictionary with personal information
my_dict = {
    "Name": "Ebrahim",          # Person's name
    "Company": "Academy",       # Company name
    "University": "DIU",        # University name
    "Phone": "01886644261",    # Phone number
    "Batch": 43                # Batch number
}

# Access an item by key using square bracket notation
print(my_dict["University"])   # Output: DIU

# Access an item using get() method
print(my_dict.get("Batch"))    # Output: 43