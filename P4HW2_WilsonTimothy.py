# Timothy Wilson
# April 13, 2025
# P4HW2_WilsonTimothy
# Calculating Total Pay



total_employees = 0
total_overtime = 0.0
total_regular = 0.0
total_gross = 0.0

while True:
    emp_name = input("Enter employee's name or \"Done\" to terminate: ")
    if emp_name == "Done":
        break

    hours = float(input(f"How many hours did {emp_name} work? "))
    rate = float(input(f"What is {emp_name}'s pay rate? "))

    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours

    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = regular_hours * rate
    gross_pay = overtime_pay + regular_pay

    
    print("\nEmployee name: ", emp_name)
    print()
    print("Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay   Gross Pay")
    print("---------------------------------------------------------------------------")
    print(f"{hours:<14.1f}{rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<14.2f}${regular_pay:<13.2f}${gross_pay:.2f}")
    print()

    
    total_employees += 1
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay


print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
