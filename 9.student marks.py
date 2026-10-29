
print("===== STUDENT MARKS MATRIX ANALYSIS =====")

students = ["Student 1", "Student 2", "Student 3"]
subjects = ["Mathematics", "Python", "English"]

marks = []

# Input marks for each student
for student in students:
    print("\nEnter marks for", student)
    student_marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(
                    input(subject + " marks (0-100): ")
                )

                if 0 <= mark <= 100:
                    student_marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    marks.append(student_marks)

# Analyze each student's performance
print("\n===== STUDENT PERFORMANCE REPORT =====")

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)

    if average >= 75:
        result = "Excellent"
    elif average >= 60:
        result = "Good"
    elif average >= 40:
        result = "Average"
    else:
        result = "Needs Improvement"

    print("\nStudent:", students[i])
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Classification:", result)

# Calculate total marks for each subject
subject_totals = []

print("\n===== SUBJECT-WISE TOTALS =====")

for j in range(len(subjects)):
    total = 0

    for i in range(len(students)):
        total += marks[i][j]

    subject_totals.append(total)
    print(subjects[j], ":", total)

# Find the highest-scoring subject
highest_total = max(subject_totals)
highest_subjects = []

for j in range(len(subjects)):
    if subject_totals[j] == highest_total:
        highest_subjects.append(subjects[j])

print("\nHighest-scoring subject(s):",
      ", ".join(highest_subjects))
print("Highest subject total:", highest_total)

print("\nAnalysis completed.")
