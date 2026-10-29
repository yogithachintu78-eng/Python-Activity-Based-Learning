
print("===== STUDENT PERFORMANCE ANALYSIS =====")

while True:
    try:
        n = int(input("Enter number of subjects: "))
        if n > 0:
            break
        print("Enter at least one subject.")
    except ValueError:
        print("Please enter a valid whole number.")

student_data = []

for i in range(n):
    print("\nSubject", i + 1)
    subject = input("Enter subject name: ")

    marks = []

    for exam in range(1, 4):
        while True:
            try:
                mark = float(
                    input(f"Enter Exam {exam} marks (0-100): ")
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student_data.append([subject] + marks)

print("\n===== PERFORMANCE REPORT =====")

for record in student_data:
    subject = record[0]
    exam1 = record[1]
    exam2 = record[2]
    exam3 = record[3]

    average = (exam1 + exam2 + exam3) / 3

    if exam3 > exam1:
        trend = "Improved"
    elif exam3 < exam1:
        trend = "Declined"
    else:
        trend = "Unchanged"

    if average < 40 or exam3 < 40:
        status = "Needs Improvement"
    else:
        status = "Satisfactory"

    print("\nSubject:", subject)
    print("Exam 1:", exam1)
    print("Exam 2:", exam2)
    print("Exam 3:", exam3)
    print("Average:", round(average, 2))
    print("Performance Trend:", trend)
    print("Status:", status)

print("\nAnalysis completed.")
