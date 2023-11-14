mathMark = -1
ictMark = -1
englishMark = -1

while (mathMark < 0 or mathMark > 100):
    mathMark = int(input("Enter a mark for Maths between 0 and 100\n"))

while (ictMark < 0 or ictMark > 100):
    ictMark = int(input("Enter a mark for ICT between 0 and 100\n"))

while (englishMark < 0 or englishMark > 100):
    englishMark = int(input("Enter a mark for English between 0 and 100\n"))

totalMark = mathMark + ictMark + englishMark
averageMark = totalMark / 3

print("The total mark is:", totalMark)
print("The average mark is:", averageMark)


