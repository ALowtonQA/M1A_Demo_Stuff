numOne = int(input("Enter the first number\n"))
numTwo = int(input("Enter the second number\n"))

print("1 - Add       +")
print("2 - Subtract  -")
print("3 - Multiply  *")
print("4 - Divide    /")
print("5 - Square    s")

#TIP: ''' can be used for multiline strings!! See below:
# print(
# '''
# 1 - Add       +
# 2 - Subtract  -
# 3 - Multiply  *
# 4 - Divide    /
# 5 - Square    s
# ''')

result = None # using None allows the variable to exist
              # so that even when invalid choices are chosen below, we can avoid an error with our final print (line 44)

selection = input("Please choose one of the options above (+, -, *, /, s)\n")

if (selection == "+"):
    result = numOne + numTwo
elif (selection == "-"):
    result = numOne - numTwo
elif (selection == "*"):
    result = numOne * numTwo
elif (selection == "/"):
    result = numOne / numTwo
elif (selection == "s"):
    choice = int(input("Which number would you like to square? (1 or 2)\n"))
    if (choice == 1):
        result = numOne ** 2
    elif (choice == 2):
        result = numTwo ** 2
    else:
        print("invalid selection")
else:
    print("invalid selection")

if (result is not None):
    print("result:", result)


    