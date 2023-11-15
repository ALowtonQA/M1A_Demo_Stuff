numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# To replace a value, use it's index
numbers[0] = 10

# add value to beginning of list
#       insert(index, value)
numbers.insert(0, "hello")

# add value to end of list
numbers.append("end!")

# remove first occurence of value from list
numbers.remove(1)

# remove specific index from list
del(numbers[0])

# loops through the list(numbers), one value at a time (num)
for num in numbers:
    print(num)

# i in range(20) means i will go from 0-19
for i in range(len(numbers)):
    print(numbers[i])

i = 0
while (i < len(numbers)):
    print(numbers[i])
    i += 1
    # i = i + 1 - this is the same as the line above

# This loop goes backwards:
# i = len(numbers) - 1
# while (i >= 0):
#     print(numbers[i])
#     i -= 1

numbers2 = []

#add 1000 values into the list
for i in range(1, 1001):
    numbers2.append(i)

print(numbers2)

# the sort() function will sort in ascending order by default
# for letters, this means alphabetical order
# sort(reverse = true) to reverse the order
letters = ["G", "F", "K", "L", "A", "Z"]
letters.sort()
print(letters)

# split can be used to split strings into a list
# you use a delimeter (such as " " or "," or "/") to split the string
# in the example below, it's a sentence where the words are separated by spaces
# therefore, the delimeter should be a space (" ")
# for something like "18/01/2023" the delimeter of these values would be "/"
sentence = "The quick brown fox The quick brown fox The quick brown fox"
words = sentence.split(" ")
print("The number of words in the sentence is", len(words))

