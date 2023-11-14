min = 1
max = 100
finalChoice = None
attempt = 1

while (attempt <= 3):
    choice = int(input("Enter a number between " + str(min) + " and " + str(max) + "\n"))
    if (choice >= 1 and choice <= 100):
        finalChoice = choice
        break
    else:
        attempt += 1

print("Chosen value is:", finalChoice)