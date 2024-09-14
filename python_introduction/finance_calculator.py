# Financial Details
income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))
rate = 0.05
#Calculate Monthly Savings and Project Annual Savings
monthly savings = monthly expenses -  monthly income
Projected annual savings = monthly savings * 12 + (monthly savings * 12 * 0.05)
#Output Results
print("monthly savings")
print("projected annual savings")
