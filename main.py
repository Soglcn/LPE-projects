#Main Menu

from functions.clear import clear
from functions.day_converter import day_converter
from functions.kg_converter import kg_converter
from functions.time_calculator import time_calculator
from functions.percentage_calculator import increase_calculator
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
                time_calculator()
                clear()
            elif mainSelection == 'LPE4':
                increase_calculator()
                clear()
        else:
            print("You typed an undefined project name, try again.")

#Run 
main_menu()