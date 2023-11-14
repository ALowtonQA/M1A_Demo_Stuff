mark = int(input("Please enter a mark between 1 and 100\n"))

if (mark < 1 or mark > 100):
    print("Error: marks must be between 1..100")
else:
    level = int(input("Please enter a student level (1 or 2)\n"))
    if (level == 1):
        if (mark < 50):
            print("Fail")
        elif (mark >= 50 and mark <= 60):
            print("Pass")
        elif (mark >= 61 and mark <= 70):
            print("Merit")
        elif (mark >= 71 and mark <= 100):
            print("Distinction")
    elif (level == 2):
        if (mark < 40):
            print("Fail")
        elif (mark >= 40 and mark <= 50):
            print("Pass")
        elif (mark >= 51 and mark <= 65):
            print("Merit")
        elif (mark >= 66 and mark <= 100):
            print("Distinction")
    else:
        print("Invalid student level. Must be 1 or 2.")        