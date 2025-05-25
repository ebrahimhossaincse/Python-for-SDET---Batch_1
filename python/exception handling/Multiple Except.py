# try:
#     value = int("10c")
# except ValueError:
#     print("ValueError")
# except TypeError:
#     print("TypeError")

def divide(x, y):
    try:
        result = x/y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("You can't divide an String - value error")
    except TypeError:
        print("You can't divide an String")
divide(1, 0)