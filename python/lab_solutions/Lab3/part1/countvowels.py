userWord = input("Enter a word\n")

vowels = 0
index = 0

while (index < len(userWord)):
    if (userWord[index] == "a" or userWord[index] == "e" or userWord[index] == "i" or userWord[index] == "o" or userWord[index] == "u"):
        vowels += 1
    index += 1

print("The number of vowels in", userWord, "is:", vowels)