
# Progressive Electricity Billing System

fixed_charge = 50
surcharge_rate = 0.05
rebate = 20

number_of_months = int(input("Enter number of months: "))

bills = []
units_list = []

for month in range(1, number_of_months + 1):
    print("\nMonth", month)

    units = int(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units! Enter a non-negative value.")
        continue

    # Calculate energy charge using slabs
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3
    else:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    # Calculate surcharge and final bill
    surcharge = energy_charge * surcharge_rate
    bill = energy_charge + fixed_charge + surcharge

    # Apply rebate
    if units <= 100:
        bill = bill - rebate

    bills.append(bill)
    units_list.append(units)

    print("Units consumed:", units)
    print("Energy charge: Rs.", round(energy_charge, 2))
    print("Fixed charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", rebate if units <= 100 else 0)
    print("Final bill: Rs.", round(bill, 2))

# Compare monthly bills
print("\n--- Monthly Bill Comparison ---")

for i in range(len(bills)):
    print("Month", i + 1, "Bill: Rs.", round(bills[i], 2))

    if i > 0 and bills[i - 1] > 0:
        increase = ((bills[i] - bills[i - 1])
                    / bills[i - 1]) * 100

        if increase > 30:
            print("Warning: Unusual increase detected!")

        print("Change from previous month:",
              round(increase, 2), "%")
