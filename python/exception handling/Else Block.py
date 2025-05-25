def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(f"The result is {result}")

divide(20,5)