# Read first line of file
file = open("students.txt", "r") # read mode
line = file.readline() # read one line
file.close() # closes the file
print(line)

# Read every line of a file
file = open("students.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    print(line)

# Read a file line by line
file = open("students.txt", "r")

for line in file:
    print(line.strip()) # remove leading and trailing whitespace (includes spaces, \n, \t)

file.close()


# Read all lines (using with)
# opening files using with will ensure the file is always automatically closed!
# you also don't need to specify "r" for read mode, as it's the default here
with open("students.txt") as file:
    lines = file.readlines() # read all lines

for line in lines:
    print(line)

# Read a file line by line using with
with open("students.txt") as file:
    for line in file:
        print(line)


# Append to a file - using with
# "a" is append mode. This means you can add to a file witout losing what's already there!
with open("students.txt", "a") as file:
    file.write("Bob, Smith, 30, 80, 70, 60\n")
    file.write("Rob, Jones, 20, 60, 80, 90\n")


# Write to a file - using with
# "w" is write mode. This will clear the entire file and start from fresh, losing everything!
# Therefore, it's used for new files
# Also, if you want to use a full path, using backslashes, don't forget to use a raw string: r"C:\.."
# Check the final slide in the powerpoint for other valid ways to include full paths like this
with open(r"C:\Users\ailow\Documents\work\QAA\1a - Copy\labs\python_work\students.txt", "w") as file:
    file.write("Bob, Smith, 30, 80, 70, 60\n")