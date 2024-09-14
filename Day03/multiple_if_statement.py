print("Welcome to the rollercoaster")

height = int(input("What's your height in cm? "))
# age = int(input("What's your age? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))

    if age < 12:
        bill = 5
        print("Child ticket are $5")
    elif age >= 12 and age <= 18:
        bill = 12
        print("Youth ticket are $12")
    else:
        bill = 20
        print("Adult ticket are $20")

    wants_pic = input("Do you want a photo taken? Y or N.")

    if wants_pic == "Y":
        bill += 5
    print(f"Your final bill is ${bill}")


else:
    print("Sorry, you have to grow taller before you can ride.")
