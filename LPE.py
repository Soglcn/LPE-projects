#Just daily usefull programs for myself. Synced!

def main_menu():
    projects = {
        'LPE1': 'Day Converter',
        'LPE2': 'Kilograms to Pounds'
    }

    while True:
        print("--------APP LIBRARY---------")
        print("Welcome... Please input the start command for the program that you want to start!")
        print("(For see all programs, please type 'S')")
        print("(For quit, type 'Q')")
        mainSelection = input("> ").upper()

        if mainSelection == 'Q':
            print("Quitting...")
            exit()
        elif mainSelection == 'S':
            print("Available projects:")
            for code, desc in projects.items():
                print(f" - {code}: {desc}")
        elif mainSelection in projects:
            if mainSelection == 'LPE1':
                day_converter()
            elif mainSelection == 'LPE2':
                kg_converter()
        else:
            print("You typed an undefined project name, try again.")

#Day Converter
def day_converter():
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

def kg_converter():
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
                main_menu() 
                return
            else:
                print("You typed a wrong key. Please type 'N' or 'Q'")



main_menu()