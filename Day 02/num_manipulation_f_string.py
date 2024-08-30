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
