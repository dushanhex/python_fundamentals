"""
Welcome! In this Dialogue, we'll explore how to write conditional statements in Python to solve a real-world problem. We'll be creating a program to determine movie ticket prices based on a customer's age.

Here's what we'll cover:

Understanding the problem and defining the pricing rules.
Identifying the components of a conditional statement.
Writing the if and elif conditions for different age groups.
Completing the conditional statement with an else condition.
Testing and refining our conditional statement.
Here are the pricing rules we'll be working with:

Children (under 12): $8
Adults (12-64): $12
Seniors (65 and over): $10

"""
#answer code
age = int(input("enter your age in years"))

if(age<12):
          price=8
          print("welcome kid")
elif (12<=age<=64):
         price=12
         print("welcome adult")
else:
         price=10
         print("welcome senior")

print("the ticket price is ",price)