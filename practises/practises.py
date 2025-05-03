#This is the part where I'm teaching things to my students by following Lacey' book!


# Using try-except is a good method for error handling and avoiding program crashes.

def oh_12():
    try:
        print("Enter the first number: ")
        first = float(input("> "))

        print("Enter the second number: ")
        second = float(input("> "))

        if second > first:
            print(f"The {second} is bigger then {first}!")
        elif first == second:
            print(f"The {first} and {second} are equal.")
        else:
            print(f"{first} is bigger then {second}!")

    except ValueError:
        print("Please input just numbers!")

oh_12()