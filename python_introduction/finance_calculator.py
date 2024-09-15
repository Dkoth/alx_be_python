# Financial Details
monthly income = float(input("Enter your monthly income:"))
monthly expenses = float(input("Enter your total monthly expenses:"))
rate = 0.05
#Calculate Monthly Savings and Project Annual Savings
monthly_savings = float(monthly_income) - float(monthly_expenses)
Projected savings = monthly savings * 12 + (monthly savings * 12 * 0.05)
#Output Results
print("monthly savings")
print("projected savings")
