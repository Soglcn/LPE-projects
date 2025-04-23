def main_menu():
    projects = {
        'LPE1': 'Day Converter'
    }

    while True:
        print("Welcome... Please input the start command for the program that you want to start!")
        print("(For see all programs, please type 'S')")
        print("(For quit, type 'Q')")
        mainSelection = input("> ").upper()

        if mainSelection == 'Q':
            print("Quitting...")
            break
        elif mainSelection == 'S':
            print("Available projects:")
            for code, desc in projects.items():
                print(f" - {code}: {desc}")
        elif mainSelection in projects:
            if mainSelection == 'LPE1':
                day_converter()
        else:
            print("You typed an undefined project name, try again.")

#Day Converter
def day_converter():
    while True: 
        print("How many days been left?")
        userInput = int(input("> "))

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



main_menu()