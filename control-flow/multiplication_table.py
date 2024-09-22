#multiplication_table.py
#Prompt User for a Number:
number = int(input("Enter a number to see its multiplication table: "))
#Generate and Print the Multiplication Table from 1 to 10:
for i in range(1, 11):
    result = number * i
    print("{number} * {i} = {result}")
