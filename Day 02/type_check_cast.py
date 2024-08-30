
# ---------Type cast-------------


# String


numChar = len(input("What's your name?"))

print(type(numChar))    # Check for type use type keyword


new_num_char = str(numChar)    # Change type int to string

print("Your name is: " + new_num_char + " Characters")


# integer

float_num = 3.1416

print(type(float_num))

new_float_num = int(float_num)

print(123 + new_float_num)


# -----------Quiz 01-------------

# Write a program that adds the digits in a 2 digit number .
# e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on line 1 .
# Your program should work for different inputs. e.g. any two-digit number.

# The last line of your program should print the result.


two_digit_num = input()
first_digit = int(two_digit_num[0])
second_digit = int(two_digit_num[1])
print(first_digit + second_digit)