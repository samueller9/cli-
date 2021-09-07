
name = "Cleetus"
age = 43
location = "Florida"
height = 48

def greeting(name, age):
    print(name.lower())

def is_grownup(age):
    print(age >= 18)

def introduction(name, location):
    print(f"Hi im {name} and im from {location}")

def too_short (height):
    if height >= 48:
        return print("You're all good to go. Have fun!")
    else :
        return print("Sorry you aren't tall enough to ride this rollercoaster")

too_short(height)
