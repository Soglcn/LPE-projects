#KG to LBS Converter
from functions.clear import clear

def kg_converter():
    clear()
    while True: 
        print("--------KG to LBS Converter---------")
        print("Please enter the weight as KG")

        try:
            kgWeight = int(input("> "))
        except ValueError:
            print("Error: Please enter a valid number!")
            continue 

        result = kgWeight * 2.204
        print("The result is: ", result, "lbs")

        while True:
            print("Type 'N' for new calculations or 'Q' for main menu")
            userInput = input("> ").upper()

            if userInput == 'N':
                break  
            elif userInput == 'Q':
                print("Exiting to the main menu...\n")
                return  
            else:
                print("You typed a wrong key. Please type 'N' or 'Q'")