# Define a nested dictionary with student information
nested_dict = {
    "student1": {
        "Name": "Tanvir",    # Name of student1
        "Batch": 1,          # Batch number of student1
        "ID": 123            # ID of student1
    },
    "student2": {
        "Name": "Kazi",      # Name of student2
        "Batch": 1,          # Batch number of student2
        "ID": 145            # ID of student2
    }
}

# Access and print the ID of student2 from the nested dictionary
print(nested_dict["student2"]["ID"])  # Output: 145