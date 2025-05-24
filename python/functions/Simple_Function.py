# Function to print a welcome message
def say_hello():
    print("Welcome to Automation Course")

# Call say_hello function
say_hello()

# Function to print a welcome message with a name
def welcome(name):
    print("Welcome to Automation Course " + name)

# Call welcome function with a name
welcome("Ebrahim")

# Function with default parameter for welcome message
def user(name="Guest"):
    print("Welcome to Automation Course " + name)

# Call user function with a name
user("Tania")

# Call user function without a name
user()