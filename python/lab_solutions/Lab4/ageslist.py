ages = [18,33,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

agesCopy = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

length = len(ages)

for age in ages:
    print(age)

for i in range(length):
    ages[i] += 1

print(ages)

# create a copy of the original list, and use that for the loop
# remove from the original list
# this prevents breaking the iterator by reducing the size of the list whilst looping through it
# general rule of thumb: Do not remove from a list, while looping through that same list with a for loop!
for age in list(ages):
    if (age < 16 or age > 65):
        ages.remove(age)
print(ages)

#Alternative solution to the "removal" exercise is to simply filter the preferred results out:
# filteredAges = []
# for age in ages:
#     if (age >= 16 and age <= 65):
#         filteredAges.append(age)
# print(filteredAges)

# Alternative solution 2
# using List Comprehension (more advanced way in python)
# ages = [age for age in ages if age >= 16 and age <= 65]
# print(ages)

count = 0
for age in ages:
    if (age <= 25 and age >= 16):
        count += 1

print("number of 16-25 year olds:", count)

ages.sort()

print(len(ages))

print("The percentage of 16-25 year olds is", (count/len(ages)) * 100, "%")