mark = int(input("Please enter a mark between 1 and 100\n"))

if (mark < 1 or mark > 100):
    print("Error: marks must be between 1..100")
elif (mark < 50):
    print("Fail")
elif (mark >= 50 and mark <= 60):
    print("Pass")
elif (mark >= 61 and mark <= 70):
    print("Merit")
elif (mark >= 71 and mark <= 100):
    print("Distinction")

