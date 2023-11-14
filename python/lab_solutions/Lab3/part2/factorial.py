userInput = int(input("Enter an integer\n"))
result = 1

for num in range(userInput, 0, -1):
    result *= num

print(result)