#Timothy Wilson
#March 2, 2025
#P1HW2
#Balancing the Budget



print("This program calculates and displays travel expenses\n")


budget = float(input("Enter Budget: "))


destination = input("\nEnter your travel destination: ")


fuel_cost = float(input("\nHow much do you think you will spend on gas? "))


accommodation_cost = float(input("\nApproximately, how much will you need for accommodation/hotel? "))


food_cost = float(input("\nLast, how much do you need for food? "))


total_expenses = fuel_cost + accommodation_cost + food_cost


remaining_balance = budget - total_expenses


print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}\n")
print(f"Fuel: {fuel_cost}")
print(f"Accommodation: {accommodation_cost}")
print(f"Food: {food_cost}\n")
print(f"Remaining Balance: {remaining_balance}")
