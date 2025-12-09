try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    # Runs only if NO exception occurred
    print(f"Success! Result: {result}")
finally:
    # Always runs, whether there was an exception or not
    print("Execution complete.")