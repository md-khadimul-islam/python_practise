# 💪 This is a difficult challenge! 💪
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.


# --------------------------------------- LOVE CALCULATOR -----------------------------------------------

print("The Love Calculator is calculating your score...")

name1 = input()
name2 = input()

combineName = name1 + name2

name = combineName.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

firstDigit = t + r + u + e


l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

sndDigit = l + o + v + e

score = int(str(firstDigit) + str(sndDigit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")

elif (score <= 40) and (score >= 50):
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}")
