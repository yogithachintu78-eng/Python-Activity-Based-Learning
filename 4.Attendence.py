
# Attendance Recovery Computation

REQUIRED_ATTENDANCE = 75

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))

# Validate input
if total_classes <= 0:
    print("Invalid input! Total classes must be positive.")

elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid input! Check the number of classes attended.")

else:
    # Calculate current attendance
    attendance = (attended_classes / total_classes) * 100

    print("\nCurrent Attendance:",
          round(attendance, 2), "%")

    if attendance >= REQUIRED_ATTENDANCE:
        print("Status: Attendance eligibility achieved.")
        print("Additional classes required: 0")

    else:
        future_classes = 0

        # Assume the student attends every future class
        while (
            (attended_classes + future_classes)
            / (total_classes + future_classes)
        ) * 100 < REQUIRED_ATTENDANCE:
            future_classes += 1

        print("Status: Attendance below 75%.")
        print("Minimum consecutive classes to attend:",
              future_classes)

        final_attendance = (
            (attended_classes + future_classes)
            / (total_classes + future_classes)
        ) * 100

        print("Attendance after attending these classes:",
              round(final_attendance, 2), "%")
