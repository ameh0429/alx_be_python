monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: ")) 

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}")

# Calculate projected savings for the year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  # Adding 5% interest
print(f"Projected savings after one year, with interest, is: ${projected_savings}")