def divide(x, y):
    try:
        result = x/y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("You can't divide by zero")

divide(2,0)