#Day Converter
from functions.clear import clear

def day_converter():
    clear()
    while True: 
        print("--------Day Converter App---------")
        print("How many days been left?")
        userInput = input("> ")
        

        if not userInput.isdigit():
            print("Error: Please enter a valid number!")
            continue 
        
        userInput = int(userInput) 

        while True: 
            print("Which time format do you prefer?")
            print("Type for = hours: 'H', for minutes: 'M' or for seconds: 'S', for back: 'B' and for quit: 'Q'")
            choosenFormat = input("> ").upper()

            hours = 24
            mins = hours * 60
            seconds = mins * 60

            if choosenFormat == 'H':
                print("You have:", userInput * hours, "hours")
            elif choosenFormat == 'M':
                print("You have:", userInput * mins, "minutes")
            elif choosenFormat == 'S':
                print("You have:", userInput * seconds, "seconds")
            elif choosenFormat == 'B': 
                print("Returning to day input...\n")
                break  
            elif choosenFormat == 'Q': 
                print("Exiting to the main menu...\n")
                return  
            else:
                print("You typed an undefined key, try again.")
