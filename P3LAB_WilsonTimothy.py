# Timothy Wilson
# March 20, 2025
# P3LAB_WilsonTimothy
# Branching


def calculate_change(amount):
    
    cents = int(round(amount * 100))

    
    denominations = {
        "Dollar": 100,
        "Quarter": 25,
        "Dime": 10,
        "Nickel": 5,
        "Penny": 1
    }

    
    result = []

    
    for name, value in denominations.items():
        count = cents // value
        cents %= value  

        if count > 0:
            
            if name == "Penny":
                if count == 1:
                    result.append(f"{count} Penny")
                else:
                    result.append(f"{count} Pennies")
            else:
                
                if count == 1:
                    result.append(f"{count} {name}")
                else:
                    result.append(f"{count} {name}s")

    
    if result:
        print("\n".join(result))
    else:
        print("No change")


amount = float(input("Enter the amount of money as a float: $"))
calculate_change(amount)
