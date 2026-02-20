# Student Grade Book Program

subjects = []
grades = []

while True:
    subject = input("Enter subject name (q to quit): ")

    if subject.lower() == "q": 
        break

    grade = float(input(f"Enter grade for {subject}: "))

    subjects.append(subject)
    grades.append(grade)

total_sum = 0
for grade in grades:
    total_sum += grade

if len(grades) > 0:
    average = total_sum / len(grades)
    
    print("\n----- YOUR ACADEMIC PROFILE -----")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {grades[i]}")
    
    print("-" * 33)
    if average >= 5:
        print(f"Congratulations! You passed. Your average is: {average:.2f}")
    else:
        print(f"Status: Failed. Your average is {average:.2f}. Better luck next time!")
else:
    print("No data was entered.")
