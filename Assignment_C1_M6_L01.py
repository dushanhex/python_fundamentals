#!/usr/bin/env python
# coding: utf-8

# ## Solve Problems with Python
# In this lab, you will use Python to solve coding challenges related to real-world scenarios. Each activity will focus on different aspects of Python such as conditional statements, iteration, and sorting techniques.

# ### Information about grading and troubleshooting
# - To receive a grade, click Submit assignment at the top of the page.
# - If you encounter problems and want to start over, you can use the ? icon on the top of the page and click Get latest version. If that doesn't work, you can submit the incomplete assignment and start a new submission.
# 
# ### Tips for completing this lab
# As you navigate this lab, keep the following tips in mind:
# - ```### YOUR CODE HERE ###``` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
# - Feel free to open the hints for additional guidance as you work on each task.
# - You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook.
# - You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook.
# - For any print statements, make sure your capitalization matches the requirements. Remember, Python considers "Discount" and "discount" as not equal.
# 
# ### Activity 1: Making Decisions with Conditional Statements
# #### Introduction
# As a data analyst for an online book store, you're tasked with analyzing customer purchasing patterns. The marketing team wants to send special discount codes to customers based on the number of books they’ve purchased. If a customer has purchased enough books, they’ll receive a discount. If they’ve purchased more, they might qualify for an even better discount.
# #### Task 1: Define a Discount Function
# You need to write a function that helps the marketing team decide which customers should receive a discount.
# 
# Define a function called ```send_discount``` that accepts two arguments:
# - ```books_purchased```: The number of books a customer has purchased.
# - ```discount_threshold```: The minimum number of books a customer needs to purchase to receive a discount.
# 
# The function must print either of the two possible messages, as shown below. Be careful not to miss the punctuation in your print statement.
# - ```Discount applied!``` if the customer qualifies for a discount.
# - ```No discount.``` if the customer does not qualify.
# 
# #### Example:
# 
# ```python
# send_discount(books_purchased=3, discount_threshold=5)
# # Output: No discount.
# 
# send_discount(books_purchased=7, discount_threshold=5)
# # Output: Discount applied!
# 
# ```
# 
# #### Code Template:

# In[1]:


def send_discount(books_purchased, discount_threshold):
    if books_purchased >= discount_threshold:
        print("Discount applied!")
    else:
        print("No discount.")


# #### Hints:
# <details>
# <summary>Hint 1</summary>
# 
# - Use an `if` statement to check if `books_purchased` meets or exceeds the `discount_threshold`.
# </details>
# 
# <details>
# <summary>Hint 2</summary>
# 
# - Use a `print` statement to display the correct message.
# </details>
# 
# #### Test Your Function:

# In[2]:


# Checking your results 
send_discount(3, 5)  # Should print No discount.
send_discount(7, 5)  # Should print Discount applied!


# #### Task 2: Add Logical Branching for Multiple Discount Levels
# The store offers an additional promotion: If a customer purchases more than a certain number of books, they’ll receive an even bigger discount. Update your function to include this second level of discounts.
# 
# Add an additional argument, `bonus_threshold`, which represents the number of books needed to receive the better discount.
# 
# The function must print one of three possible messages, as shown below. Be careful not to miss the punctuation in your print statement.
# - `Big discount applied!` if the customer qualifies for the higher discount.
# - `Discount applied!` if the customer qualifies for the regular discount.
# - `No discount.` if they do not qualify for any discount.
# 
# #### Example:
# 
# ```python
# send_discount(books_purchased=3, discount_threshold=5, bonus_threshold=10)
# # Output: No discount.
# 
# send_discount(books_purchased=7, discount_threshold=5, bonus_threshold=10)
# # Output: Discount applied!
# 
# send_discount(books_purchased=12, discount_threshold=5, bonus_threshold=10)
# # Output: Big discount applied!
# ```
# 
# #### Code Template:
# 

# In[ ]:


def send_discount(books_purchased, discount_threshold, bonus_threshold):
    if books_purchased >= bonus_threshold:
        print("Big discount applied!")
    elif books_purchased >= discount_threshold:
        print("Discount applied!")
    else:
        print("No discount.")


# #### Hints:
# 
# <details>
# <summary>Hint 1</summary>
#     
# - Start by checking if the customer qualifies for the **big discount** using an `if` statement.
# </details>
# 
# <details>
# <summary>Hint 2</summary>
#     
# - Use an `elif` to check if they qualify for the regular discount.
# </details>
# 
# <details>
# <summary>Hint 3</summary>
#     
# - Use an `else` statement to handle cases where they don't qualify for any discount.
# </details>
# 
# #### Test Your Function:

# In[ ]:


# Checking your results 
send_discount(3, 5, 10)   # Should print No discount.
send_discount(7, 5, 10)   # Should print Discount applied!
send_discount(12, 5, 10)  # Should print Big discount applied!


# ### Activity 2: Using Loops for Repetitive Tasks
# #### Introduction
# You are a product manager at a technology startup. Customers have been providing ratings for the company's latest app. The marketing team wants to categorize this feedback into three categories: "Low", "Medium", and "High" ratings. You will use Python's iteration techniques to process customer ratings efficiently.
# #### Task 1: Categorize Customer Ratings
# Define a function called `categorize_ratings` that takes a list of customer ratings as input. Each rating is a whole number between 1 and 10.
# 
# Your function will categorize the ratings as:
# - **Low** (1-4)
# - **Medium** (5-7)
# - **High** (8-10)
# 
# The output must print three statements, one for each category, in the following order (Low, then Medium, then High):
# <br>`Low: {number_of_low_ratings}`<br>
# `Medium: {number_of_medium_ratings}`<br>
# `High: {number_of_high_ratings}`<br>
# 
# #### Example:
# ```python
# # There are two ratings in the range 1-4, two ratings in the range of 5-7 and two ratings in the range 8-10
# categorize_ratings([1, 3, 5, 7, 8, 9])
# ```
# **Output:**
# <br>`Low: 2`<br>
# `Medium: 2`<br>
# `High: 2`<br>
# #### Code Template:

# In[ ]:


def categorize_ratings(ratings):
    low = 0
    medium = 0
    high = 0
    
    for rating in ratings:
        if rating >= 1 and rating <= 4:
            low += 1
        elif rating >= 5 and rating <= 7:
            medium += 1
        elif rating >= 8 and rating <= 10:
            high += 1
    
    print(f"Low: {low}")
    print(f"Medium: {medium}")
    print(f"High: {high}")
    pass


# #### Hints:
# <details>
# <summary>Hint 1</summary>
#     
# - Use a `for` loop to iterate through the `rating_list`.
# </details>
# 
# <details>
# <summary>Hint 2</summary>
#     
# - Keep a counter for each category: low, medium, and high.
# </details>
# 
# <details>
# <summary>Hint 3</summary>
#     
# - Use `if`, `elif`, and `else` to decide which category each rating falls into.
# </details>
# 
# #### Test Your Function:

# In[ ]:


# Checking your results 
# Calling categorize_ratings([1, 3, 5, 7, 8, 9])
categorize_ratings([1, 3, 5, 7, 8, 9])
print("Expected Output:\nLow: 2\nMedium: 2\nHigh: 2")


# ### Activity 3: Sorting Test Scores with Error Handling
# #### Introduction
# You are a coder working with test scores, focusing on sorting techniques and error handling in Python. You’ll use common sorting algorithms and write robust functions that account for possible errors.
# 
# #### Task 1: Creating and Sorting Test Scores
# You have a list of students and their corresponding test scores. Your task is to organize and analyze the scores using sorting algorithms and Python's error-handling mechanisms.
# #### Step 1: Create the List of Students
# Create a list called `students` that contains the following student names: John, Lisa, Mary, Chris, Linda, Matt

# In[ ]:


students = ["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]


# #### Step 2: Create a Dictionary of Test Scores
# Create a dictionary called `test_performance` and assign the following scores to each student as follows:
# - John: 87
# - Lisa: 90
# - Mary: 75
# - Chris: 100
# - Linda: 100
# - Matt: 70

# In[ ]:


test_performance = {
    "John": 87,
    "Lisa": 90,
    "Mary": 75,
    "Chris": 100,
    "Linda": 100,
    "Matt": 70
}


# #### Step 3: Extract the Scores from the Dictionary 
# Create a list called `scores` and extract each student's score using a `for` loop.

# In[ ]:


scores = []

for student in test_performance:
    scores.append(test_performance[student])


# #### Step 4: Sorting the Scores with a Custom Function 
# Define a function called `bubble_sort` that sorts the list of scores in ascending order.

# In[ ]:


def bubble_sort(scores):
    n = len(scores)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if scores[j] > scores[j + 1]:
                # Swap the elements
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
    
    return scores


# #### Step 5: Assign the Sorted Scores to `sorted_scores`
# Call the `bubble_sort` function you defined above and assign the return value to `sorted_scores`.

# In[ ]:


sorted_scores = bubble_sort(scores)


# #### Hints for Activity 3 - Task 1:
# 
# <details>
# <summary>Hint 1</summary>
#     
# - **Sorting:** For the `bubble_sort` function, focus on comparing and swapping elements.
# </details>
# 
# #### Test Your Results:

# In[ ]:


# Checking your results 
print(sorted_scores)


# #### Task 2: Calculating and Handling Errors
# #### Step 1: Calculate the Highest and Lowest Scores
# Use the `sorted_scores` list you defined above to assign the correct values to `highest_score` and `lowest_score` below.

# In[ ]:


lowest_score = sorted_scores[0]
highest_score = sorted_scores[-1]


# #### Step 2: Define a Function to Calculate the Class Average 
# Define a function called `average_class_score` to calculate the average score. Add error handling for cases when the student list is empty.

# In[ ]:


def average_class_score(scores):
    if len(scores) == 0:
        print("Error: The student list is empty")
        return None
    
    total = sum(scores)
    average = total / len(scores)
    
    return average


# #### Step 3: Calculate the Average Score
# Use the `average_class_score` function you defined above to assign the average score to `average_score` below.

# In[ ]:


average_score = average_class_score(sorted_scores)


# #### Step 4: Handle the Case of an Empty Class
# Check that the `average_class_score` function can handle an empty class list by running the following code.

# In[ ]:


empty_class = []
empty_scores = []
error_average = average_class_score(empty_class, empty_scores)


# #### Hints for Activity 3 - Task 2:
# <details>
# <summary>Hint 1</summary>
#     
# - **Error Handling:** Use `try-except` blocks to handle division by zero when calculating the average score.
# </details>
# 
# #### Test Your Results: 

# In[ ]:


# Checking your results 
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

print(f"Average Score: {average_score}")


# #### End of Lab
# By completing this lab, you’ve gained experience in writing Python functions, applying conditional logic, iterating through lists, sorting data, and handling errors. These foundational skills are essential for solving more complex real-world problems in data analysis and beyond!
