# Your Name: Timothy Wilson
# Date: April 13, 2025
# Assignment Name: P5LAB_WilsonTimothy
# Calculating change.

import random

def disperse_change(change):
    """
    This function takes a float as input, representing the change owed to the customer,
    and prints how many dollars, quarters, dimes, nickels, and pennies are required.
    """
    
    change_in_cents = round(change * 100)

    
    dollars = change_in_cents // 100
    change_in_cents %= 100

    
    quarters = change_in_cents // 25
    change_in_cents %= 25

    
    dimes = change_in_cents // 10
    change_in_cents %= 10

    
    nickels = change_in_cents // 5
    change_in_cents %= 5

    
    pennies = change_in_cents

    
    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")


def main():
    
    total_owed = round(random.uniform(0.01, 100.00), 2)
    
    
    print(f"You owe ${total_owed}")
    
    
    amount_paid = float(input("How much cash will you put in the self-checkout? "))
    
    
    change_owed = round(amount_paid - total_owed, 2)
    
    
    print(f"Change is: ${change_owed}")
    
    
    disperse_change(change_owed)


if __name__ == "__main__":
    main()
