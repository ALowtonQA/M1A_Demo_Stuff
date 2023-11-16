print("hello") # print with 1 argument

name = "anoush"

print("hello", "Andrew") # print with 2 arguments

# print concatenates with spaces and adds new line to the end.
# this line has the same output as the line above!
print("Hello" + " " + "Andrew" + "\n") 

# You can change the default separator for prints! space " " is the default!
print("hello", name, sep="-") # print with 2 arguments

# You can change the default line end for prints! newline "\n" is the default!
print("hello", end=" ")
print("there", end=" ")
print("class", end=" ")

# print seems to take a undefined (infinite) number of parameters?
print("\nhello", "there", "anoush", "how", "are", "you?", sep="-")

# function definitions
def functionNoParams():
    print("Hello")

# This function returns a value back to where it was called   
def makeFullName(first, last):
    fullName = first + " " + last
    return fullName

# This function does not return a value back, it just performs some behaviour
def makeFullNameNoReturn(first, last):
    fullName = first + " " + last
    print(fullName)

# This function can take ANY number of arguments
# They come in as a list
# You then loop through the list to deal with each value individually
def functionWithMultipleArgs(*args):
    for arg in args:
        print(arg, end=" ")

# function calls (invocations)
print(makeFullName("Anoush", "Lowton")) # because this function returns a value, we must do something with it, like print it.

fullName = makeFullName("Anoush", "Lowton") # or we could store the return value in a variable, to use later
print(fullName)

makeFullNameNoReturn("Bob", "Smith") # this function doesn't return anything, so there's no response to do anything with

functionWithMultipleArgs("hello", "there", "class", ":)") # this function can be called with ANY number of arguments :O
