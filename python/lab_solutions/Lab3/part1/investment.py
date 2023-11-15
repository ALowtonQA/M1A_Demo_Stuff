money = int(input("Enter an initial investment\n"))
target = int(input("Enter a target value\n"))
interestRate = int(input("Enter an interest rate (10 = 10%)\n"))

years = 0

while (money < target):
    money += (interestRate * money) / 100
    print(money)
    years += 1

print(years)