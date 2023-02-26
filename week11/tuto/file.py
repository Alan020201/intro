def divide(a, b):

    try:

        result = a / b

    except ZeroDivisionError:

        print("Cannot divide by zero")

    except TypeError:

        print("Both arguments must be numbers")

    else:

        print(f"Result is: {result}")

    finally:
        print("Exiting the function")
divide(10, 2) 
divide(10, "0")
divide(10, 0)