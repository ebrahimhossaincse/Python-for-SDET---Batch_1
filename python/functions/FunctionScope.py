# Function demonstrating local variable
def my_func():
    local_variable = 10  # Local variable
    print(local_variable)

# Global variable
global_variable = 20

# Function using global and parameter variables
def test_func(a):
    num = global_variable + 60 + a  # Combine global, constant, and parameter
    print(num)

# Call test_func with argument
test_func(100)

# Authentication function with parameters
def authenticate(username, password):
    if username == 'admin' and password == 'admin':
        print('Authenticated')
    else:
        print('Not Authenticated')

# Test authentication
authenticate('admin', 'admin')

# Alternative authentication function using list
def authenticate2():
    test_data = ['admin', 'admin']  # Local list
    username = test_data[0]
    password = test_data[1]
    if username == 'admin' and password == 'admin':
        print('Authenticated')
    else:
        print('Not Authenticated')