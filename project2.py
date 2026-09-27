# ==========================================
#        EXPENSE TRACKER - PROJECT 2
# ==========================================

total = 0.0

print("\n===== EXPENSE TRACKER =====")
print("Enter your expenses one by one.")
print("Enter 0 when you are finished.\n")

while True:
    try:
        expense = float(input("Enter expense amount: ₹"))

        if expense < 0:
            print("❌ Expense cannot be negative.")
            continue

        if expense == 0:
            break

        total += expense
        print(f"Added: ₹{expense:.2f}")

    except ValueError:
        print("❌ Please enter a valid number.")

print("\n============================")
print(f"💰 Total Spent: ₹{total:.2f}")
print("============================")
print("Thank you for using Expense Tracker!")