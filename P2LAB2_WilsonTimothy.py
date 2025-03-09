#Timothy Wilson
#March 9, 2025
#P2LAB2
#Access Dictionary Items


vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}


keys = vehicle_mpg.keys()
print(keys)


vehicle = input("Enter a vehicle to see its mpg: ")


if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"The {vehicle} gets {mpg} mpg.")

    
    miles = float(input(f"How many miles will you drive the {vehicle}? "))

    
    gallons_needed = miles / mpg

    
    print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
else:
    print("Invalid vehicle name. Please enter a valid vehicle from the list.")
