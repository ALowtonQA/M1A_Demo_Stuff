#worth noting, without the use of functions (not covered yet), this code will have a lot of repetitions

timeOne = input("Enter a day-time string in the format DD:HH:MM\n")
timeTwo = input("Enter a day-time string in the format DD:HH:MM\n")

timeOneSplit = timeOne.split(":")
timeTwoSplit = timeTwo.split(":")

timeOneDays = int(timeOneSplit[0])
timeOneHours = int(timeOneSplit[1])
timeOneMinutes = int(timeOneSplit[2])

timeTwoDays = int(timeTwoSplit[0])
timeTwoHours = int(timeTwoSplit[1])
timeTwoMinutes = int(timeTwoSplit[2])

while True:
    print("Time Calculator")
    print("1- Add 2 times")
    print("2- Find the difference between 2 times")
    print("3- Convert to Hours")
    print("4- Convert to Minutes")
    print("5- Convert Minutes to Time")
    print("6- Convert Hours to Time")
    print("7- Convert Days to Time")
    print("8- Exit")
    
    option = input("Enter an option: ")
    
    if option == "1":
        # Calculate the totals
        totalDays = timeOneDays + timeTwoDays
        totalHours = timeOneHours + timeTwoHours
        totalMinutes = timeOneMinutes + timeTwoMinutes
        
        # Handle rollovers (minutes -> hours and hours -> days)
        totalHours += int(totalMinutes / 60)
        totalMinutes %= 60
        totalDays += int(totalHours / 24)
        totalHours %= 24

        result = str(totalDays) + ":" + str(totalHours) + ":" + str(totalMinutes)
        print("Result:", result)
    elif option == "2":
        # Convert both times to minutes
        totalMinutesOne = timeOneDays * 24 * 60 + timeOneHours * 60 + timeOneMinutes
        totalMinutesTwo = timeTwoDays * 24 * 60 + timeTwoHours * 60 + timeTwoMinutes

        # Calculate the difference in minutes
        differenceInMinutes = totalMinutesOne - totalMinutesTwo

        if differenceInMinutes < 0:
            totalMinutes = -differenceInMinutes
            daysResult = int(totalMinutes / (24 * 60))
            totalMinutes %= 24 * 60
            hoursResult = int(totalMinutes / 60)
            minutesResult = totalMinutes % 60
        else:
            daysResult = int(differenceInMinutes / (24 * 60))
            differenceInMinutes %= 24 * 60
            hoursResult = int(differenceInMinutes / 60)
            minutesResult = differenceInMinutes % 60

        result = str(daysResult) + ":" + str(hoursResult) + ":" + str(minutesResult)
        print("Result:", result)
    elif option == "3":
        choice = int(input("would you like to use the first or second day-time you provided? (1 or 2)"))

        if (choice == 1):
            totalHours = timeOneDays * 24 + timeOneHours + timeOneMinutes / 60
        else:
            totalHours = timeTwoDays * 24 + timeTwoHours + timeTwoMinutes / 60

        print("Result:", totalHours, "hours")
    elif option == "4":
        choice = int(input("would you like to use the first or second day-time you provided? (1 or 2)"))

        if (choice == 1):
            totalMinutes = timeOneDays * 24 * 60 + timeOneHours * 60 + timeOneMinutes
        else:
            totalMinutes = timeTwoDays * 24 * 60 + timeTwoHours * 60 + timeTwoMinutes

        print("Result:", totalMinutes, "minutes")
    elif option == "5":
        minutes = int(input("Enter minutes: "))
        
        days = int(minutes / (24 * 60))
        hours = (int(minutes / 60)) % 24
        minutes = minutes % 60

        result = str(days) + ":" + str(hours) + ":" + str(minutes)

        print("Result:", result)
    elif option == "6":
        hours = float(input("Enter hours: "))
        
        days = int(hours / 24)
        hours = int(hours % 24)
        minutes = int((hours - int(hours)) * 60)

        result = str(days) + ":" + str(hours) + ":" + str(minutes)

        print("Result:", result)
    elif option == "7":
        days = int(input("Enter days: "))

        result = str(days) + ":00:00"

        print("Result:", result)
    elif option == "8":
        break
    else:
        print("Invalid option. Please select a valid option.")