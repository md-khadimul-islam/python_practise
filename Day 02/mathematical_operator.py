# -----------Operator----------

# PEMDAS    Operator always work left to right

# P -- Parentheses
# E -- Exponents
# M -- Multiplication
# D -- Division
# A -- Addition
# S -- Subtraction


# Sign example
# ()
# **
# * /
# + -

print(3 * (3 + 3) / 3 - 3)  # 7.0


print(2 * 2 + 2 / 2 - 2)  # 7.0


# Quiz 02                           --------- BMI Calculator -------

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# BMI Wikipedia Page

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


# NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.


height = input("Please enter your height: ")
weight = input("Please enter your weight: ")
actual_height = float(height)
actual_weight = float(weight)

print(int(actual_weight / (actual_height ** 2)))

print(int(actual_weight / (actual_height ** actual_height)))   # Showing wrong answer

print(int(actual_weight / (actual_height * actual_height)))


