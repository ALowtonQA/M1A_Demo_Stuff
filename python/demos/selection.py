x = int(input("Enter a number:\n"))

# if (true) then run the code within 
# otherwise run the code within the "else" block
if (x <= 10):
    print("x <= 10")
else:
    print("x > 10")

salary = 250000

# this time multiple conditions are checked
# elif means "else if"
# in other words, if the previous condition wasn't true, check this one
# once again, else is at the end to catch everything else
if (salary > 100000):
    print("Band A")
elif (salary > 55000):
    print("Band B")
elif (salary > 32000):
    print("Band C")
elif (salary > 25000):
    print("Band D")
else:
    print("Band E")


# You could use seperate if statements, not connected by "elif" 
# However, this will mean every condition is always checked
# Which couldn result in multiple prints, where you only needed

# if (salary > 100000):
#     print("Band A")

# if(salary > 55000):
#     print("Band B")

# if(salary > 32000):
#     print("Band C")

# if(salary > 25000):
#     print("Band D")

# if(salary <= 25000):
#     print("Band E")


age = 30

# Logical and: ALL conditions must be true
# Logical and "short circuits"
# When it sees False, it stops.
if (age < 50 and age > 25):
    print("Age is between 25 and 50 (not inclusive)")
else:
    print("Age is something else")

# Logical or: Only ONE condition needs to be true
# Logical or "short circuits"
# When it sees True, it stops.
if (age == 30 or age == 25):
    print("Age is 25 or 30")
else:
    print("Age is something else")

