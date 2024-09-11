
# ------------------ Practice 01 ---------------

print("Welcome to the rollercoaster!")

height = int(input("What's your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry, you have to grow taller before you can ride.")


# ------------------ Practice 02 ---------------
print("Welcome to the game mode")

age = int(input("What's your age? \n"))

if age < 5:
    print("You are child not play game")
elif age <= 5:
    print("You are child. Play the Subway Surfers")
elif age == 10:
    print("Play the football ")
elif age <= 20:
    print("Play free fire")
else:
    print("Your age is overrated. Please exercise")

# -------------- Note ------------
# == Equal to
# > Getter than
# < less than
# <= less than equal
# >= getter than equal


# --------------------- odd or even number check -------------------

number = int(input())

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is and odd number.")
