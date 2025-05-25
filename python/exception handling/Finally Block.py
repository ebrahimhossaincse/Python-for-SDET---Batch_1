def divide(x, y):
    try:
        result = x/y
    except Exception as e:
        print(e)
        print("You can't divide by zero")
    finally:
        print("Execution Completed")

divide(20,0)