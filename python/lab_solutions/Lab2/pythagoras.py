import math

print(
'''
Pythagoras Calculator  
1 -	Find the length of A given B and C  
2 -	Find the length of B given A and C 
3 -	Find the length of C given A and B
''')

selection = int(input("Please choose either option 1, 2 or 3\n"))

if (selection == 1):
    b = int(input("enter a length for side B\n"))
    c = int(input("enter a length for side C\n"))
    print("The length of side A is: ", math.sqrt(c**2 - b**2))
elif (selection == 2):
    a = int(input("enter a length for side A\n"))
    c = int(input("enter a length for side C\n"))
    print("The length of side A is: ", math.sqrt(c**2 - a**2))
elif (selection == 3):
    a = int(input("enter a length for side A\n"))
    b = int(input("enter a length for side B\n"))
    print("The length of side A is: ", math.sqrt(a**2 + b**2))
else:
    print("invalid selection")