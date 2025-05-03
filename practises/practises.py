# This is the part where I'm teaching things to my student (which is my nephew) by following Lacey's book!
# You can also follow the functions if you have the book. I added some flair by using different styles.
# def chlg_001 is also Challenge 001 in the book!

# Using try-except is a good method for error handling and avoiding program crashes.
def chlg_001():
    print("Plaese enter your first name: ")
    firstName = input("> ")
    print(f"Hi {firstName}, nice to met you!")

def chlg_002():
    print("What's your name?")
    firstName = input("> ")

    print("And you surname?")
    surName = input("> ")

    print(f"Hey, {firstName} {surName}!")

def chlg_003():
    print("What do you call a bear with no teeth?\nA gummy bear!")

def chlg_004():
    print("Enter a number to sum!")
    firstNum = int(input("> "))
    print("And the second!")
    secondNum = int(input("> "))

    result = firstNum + secondNum

    print(f"The total of the {firstNum} and {secondNum} is {result}! ")



def chlg_012():
    try:
        print("Enter the first number: ")
        first = float(input("> "))

        print("Enter the second number: ")
        second = float(input("> "))

        if second > first:
            print(f"The {second} is bigger than {first}!")
        elif first == second:
            print(f"The {first} and {second} are equal.")
        else:
            print(f"{first} is bigger than {second}!")

    except ValueError:
        print("Invalid input! Please input only numeric values.")


