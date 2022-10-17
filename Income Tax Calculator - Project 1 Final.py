#Geoffrey Chambers COP1047C - Income Tax Calculator Project 1 Fall 2022

gross_income = float(input("Enter the gross income: "))

dependents = int(input("Enter the number of dependents:  "))

income_tax = float(f'{(gross_income - (3000 * dependents) - 10000) * (20 / 100):.1f}')

print(f"The income tax is ${income_tax}")

