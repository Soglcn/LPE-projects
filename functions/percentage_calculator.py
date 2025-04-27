#Percentage Calculator           
from functions.clear import clear

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
                elif userChoice == 'B':
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

    def percentage_reduction():
        clear()
        while True:
            try:
                print("Input current value:")
                currentValue = float(input("> "))

                print("Input percentage:")
                reducePercentage = float(input("> "))

                reductionResult = currentValue - (currentValue * (reducePercentage / 100))

                print(f" The result is {reductionResult}")

                
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
            percentage_reduction()
        elif selectedWork == 'Q':
            print("Returning main menu...")
            clear()
            return
        else:
            print("You selected wrong, try again!")
            continue
