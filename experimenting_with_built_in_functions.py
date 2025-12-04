"""
Scenario: Arctic Temperatures and Type Conversions
Code Wizards, Inc, a leading data analytics firm, recognizes the value of Python's built-in functions for streamlined data manipulation and analysis. They've enlisted your expertise to showcase the power of these functions in a variety of situations.

 In Arctic Temperatures: Fun with Python Built-in Math Functions, you will:  

Analyze temperature data from Antarctica to find the highest and lowest temperatures using max() and min(), and calculate the average temperature using sum() and len().

Calculate how far below freezing the coldest temperature reached using abs(), showcasing numerical analysis capabilities. 

In Text Conversions: Python Built-in Conversion Functions you will:

Explore how to display data types of variables using the type() function.

Convert strings to integers and integers to strings, using the int() and str() functions. 

1.
Question 1
Arctic Temperatures: Fun with Python Built-in Math Functions
Math Exercise 1: Analyzing Antarctic Temperatures  
Instructions:
1. Begin with the antarctic_temperatures list, which contains the daily temperature recordings.

2. Apply the max() function to the antarctic_temperatures list to obtain the highest temperature recorded.

3. Apply the min() function on the antarctic_temperatures list to determine the lowest temperature recorded.

4. Print the highest and lowest temperatures.

5. Calculate the average temperature by summing all temperatures in the antarctic_temperatures list using the sum() function and dividing by the number of temperatures, which you can determine using the len() function. Round the calculated average temperature to one decimal place using the round() function.

6. Print the rounded average temperature.

7. Calculate the absolute value of the coldest temperature using the abs() function.

8. Print the absolute value of the coldest temperature.

"""
antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Find the highest and lowest temperatures
highest_temp = max(antarctic_temperatures)
lowest_temp = min(antarctic_temperatures)

print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")

# Calculate the average temperature
average_temp = sum(antarctic_temperatures)/len(antarctic_temperatures)
rounded_average_temp=round(average_temp)
print("Average temperature:", average_temp, "°C")

# Find the absolute value of the coldest temperature
coldest_temp_abs = abs(lowest_temp)
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")

"""
2.
Question 2
Text Conversions: Python Built-in Conversion Functions
Instructions:
1. Start with the provided variables int_value, float_value, and text_value.

2. Use the type() function to save the data type of float_value in the variable type_of_float_value where it says STEP 2: YOUR CODE HERE. The type function can be used to determine the data type of variables, and can be used to avoid errors and exceptions.

3. Use the int() function to convert the value of text_value to an integer and store in the variable text_value_as_int where it says STEP 3: YOUR CODE HERE. Even if a string holds a numeric value, it must be converted to a numeric value (int or float) to be used as part of mathematical operations.

4. Use the str() function to convert the value of int_value to a string and store in the variable int_value_as_text where it says STEP 4: YOUR CODE HERE. Often times, numeric values that will not have mathematical operations performed on them (for example, credit card numbers, serial numbers, American ZIP codes) will be converted to text.

5. The results will print. You will see the data type of the float variable, followed by the results of adding two numeric values, followed by the results of adding those same two values as strings.

"""
int_value = 15
float_value = 4.1
text_value = "33"

type_of_float_value = type(float_value)

# Convert text_value to an integer
text_value_as_int = int(text_value)

# Convert int_value to text
int_value_as_text = str(int_value)

# DO NOT CHANGE LINES BELOW
# Print the type of float_value
print("float_value type:", type_of_float_value)

# Adding text_value_as_int to int_value
print("Integer addition: Adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)

# Adding (concatenating) text values
print("Text addition: Adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)