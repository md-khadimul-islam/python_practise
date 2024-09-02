# -------------Number Manipulation--------------

float_num = 8 / 3   # when use (8 // 3) this type result showing integer

print(float_num)   # without manipulation

# showing integer

print(int(float_num))   # int type cast


# when need . after value 2 (Note: You can use any number)
print(round(float_num, 2))


# Also you can use ( -= , *= , /= , += ) when need previous value +, -, /,  * new value
float_num += 2
print(float_num)

float_num -= 2
print(float_num)

float_num *= 2
print(float_num)

float_num /= 2
print(float_num)


# ------------- f- String ------------

score = 50
height = 5.6

print(f"Your score is: {score}\nYour height is: {height}")


# -----------Quiz 03-------------
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.

# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.


per_years = 52

age = int(input("Please enter your age "))

alive_age = 90

actual_age = 90 - age

left_weeks = f"You have {actual_age * per_years} weeks left"

print(left_weeks)
