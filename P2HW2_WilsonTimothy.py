# Timothy Wilson
# March 14, 2025 
# P2HW2_WilsonTimothy
# Entering grades for six modules 
# stores them in a list
# highest grade, sum of all grades, and the average of the grades.


# 1. Prompt the user to enter grades for Module 1 to Module 6 separately.
# 2. Store the grades in a list called 'grades'.
# 3. Calculate the lowest grade using min().
# 4. Calculate the highest grade using max().
# 5. Calculate the sum of the grades using sum().
# 6. Calculate the average of the grades.
# 7. Display the results formatted as shown in the sample output.


grades = []  

grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))


lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)


print("\n------------Results------------")
print(f"Lowest Grade:    {lowest_grade:.1f}")
print(f"Highest Grade:   {highest_grade:.1f}")
print(f"Sum of Grades:   {sum_of_grades:.1f}")
print(f"Average:         {average_grade:.2f}")
print("--------------------------------")
