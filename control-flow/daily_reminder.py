#daily_reminder.py
#Prompt for a Single Task 
task = input("Enter your task:")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
#Process the Task Based on Priority and Time Sensitivity:
match priority:
    case "high":
        reminder = "'{task}' is a high priority task."
    case "medium":
        reminder = "'{task}' is a medium priority task."
    case "low":
        reminder = "'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority entered. Please enter high, medium, or low."
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."
print("Reminder: {reminder}")
