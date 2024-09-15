# Financial Details
income = float(input("Enter your monthly income:"))
expenses = float(input("Enter your total monthly expenses:"))
rate = 0.05
#Calculate Monthly Savings and Project Annual Savings
monthly_savings = monthly expenses -  monthly income
Projected_annual savings = monthly savings * 12 + (monthly savings * 12 * 0.05)
#Output Results
print("monthly_savings")
print("projected_annual_savings")
