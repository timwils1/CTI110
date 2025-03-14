#Timothy Wilson
#March 14, 2025
#P2HW1
#Calculating and Displaying Travel Expenses


    
def travel_expenses():
    print("This program calculates and displays travel expenses")
    
    budget = float(input("Enter Budget: "))
    destination = input("Enter your travel destination: ")
    gas = float(input("How much do you think you will spend on gas? "))
    accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
    food = float(input("Last, how much do you need for food? "))

    total_expenses = gas + accommodation + food
    remaining_balance = budget - total_expenses

    print("\n------------Travel Expenses------------")
    print(f"Location:       {destination}")
    print(f"Initial Budget: ${budget:.2f}")
    print(f"Fuel:           ${gas:.2f}")
    print(f"Accommodation:  ${accommodation:.2f}")
    print(f"Food:           ${food:.2f}")
    print("--------------------------------------")
    print(f"Remaining Balance: ${remaining_balance:.2f}")


travel_expenses()
