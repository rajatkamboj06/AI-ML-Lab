# Prompt the user to enter a number
number = int(input("Enter the number you want to get checked: "))

# Use the modulus operator to check if the number is even or odd
if (number % 2) == 0:
    print("The number given is even.")
else:
    print("The number given is odd.")
