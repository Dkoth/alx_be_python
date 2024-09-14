# Financial Details
monthly_income = int(input("Enter your monthly_income:"))
monthly_expenses = int(input("Enter your total monthly_expenses:"))
rate = 0.05
#Calculate Monthly Savings and Project Annual Savings
monthly_savings = monthly_expenses -  monthly_income
Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
#Output Results
print("monthly_savings")
print("projected_savings")
