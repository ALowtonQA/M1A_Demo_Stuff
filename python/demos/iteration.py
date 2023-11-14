# While Loops
x = 1
while (x < 5):
    print("The value is:", x)
    x = x + 1
    # x += 1 - this is the same as the line above!

n = 1
while (n <= 5):
    print("*" * n) #print "*" n number of times
    n = n + 1
    # n += 1 - this is the same as the line above!
print("*" * n) # ******

while (n > 0):
    n = n - 1
    # n -= 1 - this is the same as the line above!
    print("*" * n)

# Example of infinite loop, that you break from manually, using "break"
while (True):
    userInput = int(input("Enter a number:\n"))

    if (userInput == 5 or userInput == 10):
        break

total = 0
choice = "y"
while (choice == "y"):
    total += int(input("Enter a number (1-10)\n"))

    if (total >= 21):
        break # exit the loop entirely here
    
    # if a choice besides "y" is chosen, the loops will end because of the loop condition on line 29
    choice = input("Would you like to give another number? y or n\n")

print("total is", total)


# range function
range(5)        # 0,1,2,3,4
range(1,5)      # 1,2,3,4
range(5, 0, -1) # 5,4,3,2,1

# for loops
for i in range(1, 6):
    print(i) # 1, 2, 3, 4, 5

for i in range(6, 0, -1):
    print(i) # 6, 5, 4, 3, 2, 1
