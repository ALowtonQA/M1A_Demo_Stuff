import statistics

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",")

grades = list(map(int, grades))

min = min(grades)
print("The minimum value is", min)

max = max(grades)
print("The maximum value is", max)

mean = round(statistics.mean(grades), 2)
# print("The mean is", round(sum(grades)/len(grades), 2))
print("The mean is", mean)

median = statistics.median(grades)
print("The median is", median)

print("The min is {}, the max is {}, the mean is {}, and the median is {}".format(min, max, mean, median))

