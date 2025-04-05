# Timothy Wilson
# April 13, 2025
# P4HW1 Score Grades



num_scores = int(input("How many scores do you want to enter? "))


scores = []


for i in range(1, num_scores + 1):
    while True:
        score = float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i} again:")


lowest_score = min(scores)
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
average = sum(modified_scores) / len(modified_scores)


if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"


print("\n-------------Results-------------")
print(f"Lowest Score   : {lowest_score:.1f}")
print(f"Modified List  : {modified_scores}")
print(f"Scores Average : {average:.2f}")
print(f"Grade          : {grade}")
print("---------------------------------")
