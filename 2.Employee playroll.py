
# Employee Payroll and Deduction Analysis

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
overtime_hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive amount: "))

# Validate input
if basic_salary < 0 or overtime_hours < 0 or incentive < 0:
    print("Invalid input! Values cannot be negative.")

else:
    # Calculate allowances
    hra = basic_salary * 20 / 100
    other_allowance = basic_salary * 10 / 100

    # Calculate overtime pay
    overtime_pay = overtime_hours * 100

    # Calculate gross salary
    gross_salary = (
        basic_salary
        + hra
        + other_allowance
        + overtime_pay
        + incentive
    )

    # Calculate deductions
    deduction = gross_salary * 5 / 100

    if gross_salary > 20000:
        deduction = deduction + 200

    # Calculate net salary
    net_salary = gross_salary - deduction

    # Display salary statement
    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name       :", employee_name)
    print("Basic Salary        : Rs.", round(basic_salary, 2))
    print("HRA                 : Rs.", round(hra, 2))
    print("Other Allowance     : Rs.", round(other_allowance, 2))
    print("Overtime Pay        : Rs.", round(overtime_pay, 2))
    print("Incentive           : Rs.", round(incentive, 2))
    print("--------------------------------------")
    print("Gross Salary        : Rs.", round(gross_salary, 2))
    print("Total Deductions    : Rs.", round(deduction, 2))
    print("Net Salary          : Rs.", round(net_salary, 2))
    print("======================================")
