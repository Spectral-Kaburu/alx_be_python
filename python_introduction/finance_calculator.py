income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income - expenses
interest = savings * 12 * 0.05
projected_savings = savings * 12 + interest
print(f"Your monthly savings are: ${savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
