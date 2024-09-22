#pattern_drawing.py
#Prompt User for Pattern Size:
length = int(input("Enter the size of the pattern: "))
#Initializing row
row = 0
#Draw the Pattern:
while row < length:
    for col in range(length):
        print("*", end="")
    print()
    row += 1
