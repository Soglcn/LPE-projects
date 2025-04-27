#Time Calculator

from functions.clear import clear

def time_calculator():
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
