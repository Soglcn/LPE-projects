#Just daily usefull programs for myself. 260425-Updated!
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Main Menu
def main_menu():
    clear()
    projects = {
        'LPE1': 'Day Converter',
        'LPE2': 'Kilograms to Pounds',
        'LPE3': 'Sleep Calculator',
        'LPE4': 'Increase Calculator'
    }

    while True:
        print("--------APP LIBRARY---------")
        print("Welcome... Please input the start command for the program that you want to start!")
        print("(For see all programs, please type 'S')")
        print("(For quit, type 'Q')")
        mainSelection = input("> ").upper()

        if mainSelection == 'Q':
            print("Quitting...")
            clear()
            exit()
        elif mainSelection == 'S':
            print("Available projects:")
            for code, desc in projects.items():
                print(f" - {code}: {desc}")
            input("\n(Press Enter to return to the main menu)")
        elif mainSelection in projects:
            if mainSelection == 'LPE1':
                day_converter()
                clear()
            elif mainSelection == 'LPE2':
                kg_converter()
                clear()
            elif mainSelection == 'LPE3':
                sleep_calculator()
                clear()
            elif mainSelection == 'LPE4':
                increase_calculator()
                clear()
        else:
            print("You typed an undefined project name, try again.")

#Day Converter
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

#KG Converter
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
                main_menu() 
                return
            else:
                print("You typed a wrong key. Please type 'N' or 'Q'")

#Time Calculator
def sleep_calculator():
    clear()
    while True:
        minutes = 60

        try:
            print("--------Sleep Calculator App---------")
            print("When did you hit the bed? (Hour, 0-23)")
            bedHourInput = input("> ")

            if not bedHourInput.isdigit() or len(bedHourInput) > 2:
                print("Error: Please enter a valid hour (0-23) with max 2 digits!")
                continue
            bedHour = int(bedHourInput)
            if bedHour > 23:
                print("Error: Hour must be between 0-23!")
                continue

            print("Minutes? (0-59)")
            bedMinInput = input("> ")

            if not bedMinInput.isdigit() or len(bedMinInput) > 2:
                print("Error: Please enter valid minutes (0-59) with max 2 digits!")
                continue
            bedMinutes = int(bedMinInput)
            if bedMinutes > 59:
                print("Error: Minutes must be between 0-59!")
                continue

            print("When did you wake up? (Hour, 0-23)")
            wakeHourInput = input("> ")

            if not wakeHourInput.isdigit() or len(wakeHourInput) > 2:
                print("Error: Please enter a valid hour (0-23) with max 2 digits!")
                continue
            wakeHour = int(wakeHourInput)
            if wakeHour > 23:
                print("Error: Hour must be between 0-23!")
                continue

            print("Minutes? (0-59)")
            wakeMinInput = input("> ")

            if not wakeMinInput.isdigit() or len(wakeMinInput) > 2:
                print("Error: Please enter valid minutes (0-59) with max 2 digits!")
                continue
            wakeMinutes = int(wakeMinInput)
            if wakeMinutes > 59:
                print("Error: Minutes must be between 0-59!")
                continue

        except ValueError:
            print("Please enter numbers only!")
            continue

        bedTotal = bedHour * minutes + bedMinutes
        wakeTotal = wakeHour * minutes + wakeMinutes

        if wakeTotal < bedTotal:
            wakeTotal += 24 * minutes  

        totalSleep = wakeTotal - bedTotal
        sleepHour = totalSleep // minutes
        sleepMin = totalSleep % minutes

        print(f"\nYou slept for {int(sleepHour)} hour(s) and {sleepMin} minute(s).\n")

        while True:
            print("Type 'N' for a new calculation or 'Q' for main menu.")
            userInput = input("> ").upper()

            if userInput == 'N':
                break  
            elif userInput == 'Q':
                return  
            else:
                print("You typed a wrong key. Please type 'N' or 'Q'.")

#Percentage Calculator           
def increase_calculator():
    clear()
    def increment():
        clear()           
        while True:
            try:
                print("Input your starting number: ")
                userValue = float(input("> "))

                print("Input your increment percentage: ")
                percentage = float(input("> "))
            
                rate = percentage / 100
                increasedValue = userValue * rate
                resultIncreasing = userValue + increasedValue

                print(f"Result after {percentage}% increment: {resultIncreasing}\n") 

                while True:
                    print("'N' for new calculation or 'B' for back")
                    menuSelection = str(input("> ")).upper()

                    if menuSelection == 'N':
                        break
                    elif menuSelection == 'B':
                        return 
                    else:
                        print("You selected wrong, try again!\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

    def findPercentage():
        clear()
        while True:
            try:
                print("Input the value: ")
                fpValue = float(input("> "))

                print("Input the percentage ratio: ")
                fpPercentage = float(input("> "))

                fpResult = (fpValue * fpPercentage) / 100
                print(f" {fpPercentage}% of the {fpValue} is {fpResult:.2f}")

                print("Press 'N' for new calculation , Press 'B' for main menu. ")
                userChoice = str(input("> ")).upper()

                if userChoice == 'N':
                    continue
                    clear()
                elif userChoice == 'Q':
                    return
                else:
                    print("You selected wrong, try again!\n")

            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

    def percentage_change():
        clear()
        while True:
            try:
                print("Input current value:")
                currentNum = float(input("> "))

                print("Input old value: ")
                oldValue = float(input("> "))

                changeValue = (currentNum - oldValue) / oldValue * 100

                print(f" The changes between of {currentNum} and {oldValue} is {changeValue:.2f}%")

                while True:
                    print("'N' for new calculation or 'B' for back")
                    menuSelection = input("> ").upper()

                    if menuSelection == 'N':
                        break
                    elif menuSelection == 'B':
                        return
                    else:
                        print("You selected wrong, try again!\n")
            
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
    
    while True:
        clear()
        print("Select the calculating type:")
        print("- 'I' for Increment by Percentage")
        print("- 'F' for Find Percentage of a Value")
        print("- 'C' for Percentage Change")
        print("- 'R' for Percentage Reduction")
        print("- 'Q' for to return main menu")
        
        selectedWork = str(input("> ")).upper()
        
        if selectedWork == 'I':
            increment()
        elif selectedWork == 'F':
            findPercentage()
        elif selectedWork == 'C':
            percentage_change()
        elif selectedWork == 'R':
            print("R")
        elif selectedWork == 'Q':
            print("Returning main menu...")
            clear()
            return
        else:
            print("You selected wrong, try again!")
            continue

#Run
main_menu()
