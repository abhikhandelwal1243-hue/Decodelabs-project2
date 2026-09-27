💰 Expense Tracker – Project 2

A simple and beginner-friendly Expense Tracker built with Python that allows users to enter multiple expenses, calculates the total amount spent, and handles invalid or negative inputs safely.

📌 Project Overview

The Expense Tracker is a console-based Python application designed to make basic expense calculation simple and interactive.

Users can:

Enter expenses one by one
Add multiple expenses
Prevent negative expense values
Handle invalid input without crashing
Stop entering expenses by entering 0
View the total amount spent
✨ Features

💵 Add Expenses – Enter expenses individually.
➕ Automatic Total – Calculates the total of all entered expenses.
🚫 Negative Value Validation – Prevents negative expense amounts.
⚠️ Input Validation – Handles invalid inputs using try-except.
🎯 Exit Option – Enter 0 to finish entering expenses.
📊 Formatted Output – Displays amounts with two decimal places.
🖥️ Simple Console Interface – Easy to use for beginners.
🛠️ Technologies Used

Python 3
while loop
if-else
try-except
float()
Formatted strings (f-strings)
🔄 How It Works

Start
  ↓
Enter Expense
  ↓
Is the input valid?
  ├── No → Show error → Enter again
  └── Yes
       ↓
Is expense negative?
  ├── Yes → Show error → Enter again
  └── No
       ↓
Is expense 0?
  ├── Yes → Stop
  └── No → Add to Total
              ↓
         Enter next expense
              ↓
           Total Spent
▶️ How to Run

1. Clone the repository

git clone https://github.com/khandelwalabhi59846-cpu/Decodelabs-internship-project2.git
2. Open the project

cd Decodelabs-internship-project2
3. Run the Python program

python3 expense_tracker.py
Replace expense_tracker.py with your actual Python filename if it is different.
💻 Example Output

===== EXPENSE TRACKER =====
Enter your expenses one by one.
Enter 0 when you are finished.

Enter expense amount: ₹250
Added: ₹250.00

Enter expense amount: ₹100.50
Added: ₹100.50

Enter expense amount: ₹50
Added: ₹50.00

Enter expense amount: ₹0

============================
💰 Total Spent: ₹400.50
============================
Thank you for using Expense Tracker!
🎯 Learning Objectives

This project helped me practice:

Python variables
User input
Type conversion
Loops
Conditional statements
Exception handling
Basic arithmetic operations
String formatting
Input validation
🚀 Future Improvements

The project can be extended with:

📅 Expense dates
🏷️ Expense categories
📊 Category-wise spending
💾 Saving expenses to a file
📈 Monthly expense reports
🔍 Expense search
🖥️ Graphical User Interface (GUI)
🗄️ Database integration
👨‍💻 Author

Abhishk Sharma

⭐ Project Status

Completed – Project 2

This project was created as part of my Python programming/internship learning journey.

If you find this project useful, consider giving the repository a ⭐.
