#Timothy Wilson
#April 13, 2025
#P4LAB2_WilsonTimothy
#Positive and Negative Integers


run_again = "yes"

while run_again.lower() == "yes":
    number = int(input("Enter an integer: "))

    if number < 0:
        print("This program does not handle negative numbers.\n")
    else:
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")
        print()

    run_again = input("Would you like to run the program again? ")

print("\nExiting program...")
