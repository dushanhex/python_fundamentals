"""
Step 1: Store temperature data
Instructions:
You need two lists to store temperature data.

The first list, celsius_temperatures,  has been created for you.

Add the following sample Celsius temperatures to it: 0, 10, 25, 32, 100 to celsius_temperatures.

Create the second list, fahrenheit_temperatures, as an empty list to store the converted Fahrenheit temperatures later. It should be an empty list right now.

Print both lists to observe their initial state.
"""
# Create a list and add sample Celsius temperatures to it 
celsius_temperatures = [] # Start with an empty list (do not modify)

# Add the Celsius temperatures to the list
celsius_temperatures.append(0)
celsius_temperatures.append(10)
celsius_temperatures.append(25)
celsius_temperatures.append(32)
celsius_temperatures.append(100)

# Create an empty list to store Fahrenheit temperatures
fahrenheit_temperatures = []

# Print both lists (do not modify)
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures) 

"""
Step 2: Convert temperatures
Instructions:
It's time to convert your Celsius temperatures to Fahrenheit:

A for loop to iterate through each celsius value in the celsius_temperatures list has been provided for you. 

Inside the loop:

Apply the Celsius to Fahrenheit conversion formula: F = (C * 9/5) + 32, where F is the Fahrenheit temperature and C is the Celsius temperature. Please use the formula as shown above.

The code to store each calculated fahrenheit value in the fahrenheit_temperatures list using the append() method has been provided for you. 

Print the results.
"""
# Lists from Step 1 (do not modify)
celsius_temperatures = [0, 10, 25, 32, 100]
fahrenheit_temperatures = [] 

# Convert each Celsius temperature to Fahrenheit
for celsius in celsius_temperatures:  # Start the loop (do not modify this line)
  fahrenheit = (celsius*9/5) + 32

  fahrenheit_temperatures.append(fahrenheit)  # Append to the list (do not modify this line)

# Print the results (including the output from Step 1 - do not modify)
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)

