userWord = input("Enter a word\n")

vowels = 0

for char in userWord:
    if char in "aeiou":
        vowels += 1

print("The number of vowels in", userWord, "is:", vowels)