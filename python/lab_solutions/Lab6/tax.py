def calculate_tax(salary):
    personalAllowance = 11850
    totalTax = 0

    if salary <= personalAllowance:
        return 0  # No tax if salary is less than or equal to the personal allowance

    # Calculate tax for the 20% bracket
    if salary <= 34500:
        totalTax += (salary - personalAllowance) * 0.2
        return totalTax

    totalTax += (34500 - personalAllowance) * 0.2

    # Calculate tax for the 40% bracket
    if salary <= 150000:
        totalTax += (salary - 34500) * 0.4
        return totalTax

    totalTax += (150000 - 34500) * 0.4

    # Calculate tax for the 45% bracket
    totalTax += (salary - 150000) * 0.45

    return totalTax

print(calculate_tax(130000))