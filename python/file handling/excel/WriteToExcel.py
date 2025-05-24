# Import the pandas library for data manipulation
import pandas as pd

# Define a dictionary with student information
dict = {
    "Name": ["Tanvir", "Etu", "Fahmida", "Tania", "Sazzad", "Sajid"],  # List of names
    "ID": [10, 12, 55, 66, 22, 44]                                    # List of IDs
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data=dict)

# Print the DataFrame to display its contents
print(df)

# Save the DataFrame to an Excel file without including the index column
df.to_excel("data.xlsx", index=False)