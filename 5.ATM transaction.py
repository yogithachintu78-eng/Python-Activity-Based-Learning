
# ATM Transaction Sequence Simulation

balance = 5000.0
withdrawal_limit = 2000.0
transaction_history = []

print("===== WELCOME TO PYTHON ATM =====")
print("Initial Balance: Rs.", balance)

number_of_transactions = int(
    input("Enter number of transactions: ")
)

if number_of_transactions < 0:
    print("Invalid number of transactions.")

else:
    for i in range(number_of_transactions):
        print("\nTransaction", i + 1)

        transaction_type = input(
            "Enter deposit or withdraw: "
        ).strip().lower()

        amount = float(input("Enter amount: Rs. "))

        if amount <= 0:
            status = "Rejected: Invalid amount"

        elif transaction_type == "deposit":
            balance += amount
            status = "Successful deposit"

        elif transaction_type == "withdraw":
            if amount > withdrawal_limit:
                status = "Rejected: Withdrawal limit exceeded"
            elif amount > balance:
                status = "Rejected: Insufficient balance"
            else:
                balance -= amount
                status = "Successful withdrawal"

        else:
            status = "Rejected: Invalid transaction type"

        transaction_history.append(
            (transaction_type, amount, status, balance)
        )

        print("Status:", status)
        print("Current Balance: Rs.", round(balance, 2))

    # Display transaction summary
    print("\n===== TRANSACTION SUMMARY =====")

    for transaction in transaction_history:
        kind, amount, status, current_balance = transaction

        print(
            kind.title(),
            "| Amount: Rs.", round(amount, 2),
            "|", status,
            "| Balance: Rs.", round(current_balance, 2)
        )

    successful_deposits = sum(
        1 for t in transaction_history
        if t[0] == "deposit" and t[2] == "Successful deposit"
    )

    successful_withdrawals = sum(
        1 for t in transaction_history
        if t[0] == "withdraw" and t[2] == "Successful withdrawal"
    )

    rejected_transactions = sum(
        1 for t in transaction_history
        if t[2].startswith("Rejected")
    )

    print("\nSuccessful Deposits:", successful_deposits)
    print("Successful Withdrawals:", successful_withdrawals)
    print("Rejected Transactions:", rejected_transactions)
    print("Final Balance: Rs.", round(balance, 2))
    print("================================")
