
print("===== ADVANCED NUMERIC PATTERN GENERATOR =====")

try:
    rows = int(input("Enter the number of rows (1-10): "))

    if rows < 1 or rows > 10:
        print("Invalid input! Enter a number from 1 to 10.")

    else:
        # Pattern 1: Increasing numbers
        print("\nPattern 1: Increasing Numbers")

        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

        # Pattern 2: Repeated row numbers
        print("\nPattern 2: Repeated Row Numbers")

        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(i, end=" ")
            print()

        # Pattern 3: Inverted numbers
        print("\nPattern 3: Inverted Number Pattern")

        for i in range(rows, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

except ValueError:
    print("Invalid input! Please enter a whole number.")

print("\nPattern generation completed.")
