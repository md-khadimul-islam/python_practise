print("Welcome to the rollercoaster")

height = int(input("What's your height in cm? "))
# age = int(input("What's your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age < 12:
        print("Please pay $5")
    elif age >= 12 and age <= 18:
        print("Please pay $12")
    elif age>=45 and age<= 55:
              print("Please join for free")
    else:
        print("Please pay $20")
else:
    print("Sorry, you have to grow taller before you can ride.")
