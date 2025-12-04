"""
Scenario: Scoping out Functions
Code Wizards, Inc, a leading data analytics firm, has enlisted your help to demonstrate the concepts of functions and scope to students who will be attending a career day event at your location. The instructional team has provided you with the examples below. You will work through them to test. Since you will be dealing with beginners, you will try to follow the examples as written and avoid advanced material (such as type hints) or improving the code when practicing the demo.

In Scoping out Functions, you will:

Create a function with no parameters and no return value.

Create a function with parameters and no return value.

Create a function with no parameters and a return value.

Create a function with parameters and a return value.

Create an example to demonstrate variable scope.

Create an example to demonstrate module imports.

Exercise 1: No Parameters, No Return Value
Instructions:
In this example, you will write a function that takes no parameters and will display a standard message. 

The starting code has a call to a function, happy_birthday, that you will be writing.

Write the function definition for the function, happy_birthday, which takes no parameters (1 line of code). Avoid type hints for the parameters.

The function should print Happy Birthday! to the user (1 line of code). The function should not return a value. Make sure the capitalization matches exactly (capital H, and capital B), and that you include the exclamation point.

Run the program. The program will always display the same message.

"""
def happy_birthday():
    print("Happy Birthday!")

# Code to call the function
happy_birthday()

"""
Exercise 2: Parameters, but No Return Value  
Instructions
In this example, you will write a function that takes two parameters and will display a customized message. 

The starting code has a call to a function, happy_birthday, that you will be writing.

Write the function definition for the function, happy_birthday, which takes two parameters, the first named age and the second named name (1 line of code). Avoid type hints for the parameters.

The function should print Happy Birthday <name> and congratulations on turning <age> years old! to the user (1 line of code). For example, if you pass the values 22 for age and Nora for name, the program should display Happy Birthday Nora and congratulations on turning 22 years old! The function should not return a value. Ensure the spacing is consistent with the requirements (for example, "Happy Birthday  Nora" has two spaces between "Birthday" and "Nora" when it should have one).

Run the program. As it is currently written, it will always display the same message, but it could be modified to accept input instead of always using the same values.
"""
def happy_birthday(age,name):
    print(f"Happy Birthday {name} and congratulations on turning {age} years old!")

# Code to call the function
happy_birthday(22, "Nora")

"""
Exercise 3: No Parameters, but a Return Value
Instructions
In this example, you will create a function to generate a lucky number. By declaring it as a function, this code can be re-used in other parts of the program. By having the definition in one place, it would allow you to change the functionality in many places by changing one line in the function.

Begin by writing the function definition for a get_lucky_number function. Remember, this function should not require any input parameters (one line of code). Avoid type hints for the return value.

The function should then return the value of lucky_num (one line of code). The value has already been loaded; your task is to return the value to the main program.

Run the program. A random number will be generated in the range (1 to 100, as defined in the function). This allows the logic to be written once and re-used many times in the program.
"""
import random

def get_lucky_number():
  lucky_num = random.randint(1,100)
  return lucky_num

# Get a lucky number between 1 and 100
lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)

"""
Exercise 4: Parameters and Return Value  
Instructions
In this example, you will write a function to calculate the discounted total based on whether a user is a member of the discount club or not.

Begin by writing the function definition for the calc_sale_price function. This function will accept two input parameters (one line of code). The first, amount, is a number representing the amount of purchase. The second, member, is a boolean variable representing whether the user is a member (True) or not (False). Avoid type hints for the parameters and return type.

Round amount to two decimal places using the built-in function round. Save the result in the amount variable.

The function should then return the value of amount. 

Run the code. The discounted amounts will be displayed.
"""
def calc_sale_price(amount,member):
	if member:
		# Members receive a 15% discount (0.15)
		amount = amount - (amount * 0.15)
	else:
		# Non-members get a 5% discount (0.05)
		amount = amount - (amount * 0.05)

	# Round amount to two decimal places
	# Save back in the amount variable
	amount = round(amount,2)

	# Return amount to the main program
	return amount

# Example price (already provided)
full_price = 150.50

# Call function for members
member_price = calc_sale_price(full_price, True)
print("Member price:",member_price)

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:",non_member_price)

"""
Exercise 5: Scope
Instructions
In this example, you will explore the concept of scope.

1. Run the code below and note the error. The first function call, display_color_works(), will successfully run. The second, display_color_failure(), will result in a NameError.

2. There are a few ways to correct this. 

     a. One way is to comment out the line calling the display_color_failure. This does not fix the problem, but it avoids the error.

     b. The preferred way is to set the shirt_color outside of the display_color_works function, in the main program, and pass the value to both functions.

     c. A third way is to catch the error using a try/catch block.

     d. A fourth way is to declare the variable as a global variable, but as discussed in an earlier reading, this is considered bad practice.

3. Comment out the call to the display_color_failure function and re-run the program. Verify the error disappears. 
code - 
def display_color_works():
  shirt_color = "Pink"
  print("First shirt color is:", shirt_color)
  
def display_color_failure():
  # Try to access 'color' directly (this will cause an error)
  print("Your shirt color is:", shirt_color)

# The shirt_color variable is in scope in this function
display_color_works()

# The shirt_color variable is not in scope in this function
#display_color_failure()

Exercise 6: Importing a module  
Instructions
In this example, you will examine using functions from another module.

You have created a file named menus.py stored in the same folder as your current program. This module contains a function, display_menu, that has been written. It takes no arguments and returns a numeric value.

Import the menus module to make the contents available to your program.

Enter the code to call the display_menu module in the menus module. The result will be saved in the user_choice variable.

This code requires a menus.py file. It will work on the Coursera platform, but it would not work in a separate code editor on your system. Designing this way allows another programmer to modify the menus module independently of your code, and your program will benefit from the latest update.

code - 
import menus


# Call the display_menu function in the menus module
user_choice = menus.display_menu()

print(user_choice)

"""