

import tkinter as tk
from tkinter import messagebox
import os
import datetime

# Initialize expense file
def initialize_file():
    if not os.path.exists('expenses.txt'):
        with open('expenses.txt', 'w') as file:
            file.write('Date, Amount, Category, Description\n')

# Add expense to the file
def add_expense(date, amount, category, description):
    with open('expenses.txt', 'a') as file:
        file.write(f'{date},{amount},{category},{description}\n')
    messagebox.showinfo("Success", "Expense added")

# View all expenses
def view_expenses():
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
    expenses_text.delete(1.0, tk.END)  # Clear the current text
    expenses_text.insert(tk.END, ''.join(lines))  # Insert the expenses

# Filter expenses by date or category
def filter_expenses():
    filter_by = filter_by_var.get()
    filter_value = filter_value_entry.get()
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
    filtered_expenses = []
    for line in lines:
        data = line.strip().split(',')
        if filter_by == 'date' and filter_value == data[0]:
            filtered_expenses.append(line)
        elif filter_by == 'category' and filter_value == data[2]:
            filtered_expenses.append(line)
    expenses_text.delete(1.0, tk.END)
    expenses_text.insert(tk.END, ''.join(filtered_expenses))

# Delete an expense
def delete_expense():
    date = delete_date_entry.get()
    amount = delete_amount_entry.get()
    category = delete_category_entry.get()
    description = delete_description_entry.get()
    lines = []
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
    with open('expenses.txt', 'w') as file:
        for line in lines:
            if line.strip() != f'{date},{amount},{category},{description}':
                file.write(line)
    messagebox.showinfo("Success", "Expense deleted")

# Show monthly summary
def monthly_summary():
    current_month = datetime.datetime.now().strftime('%Y-%m')
    total_expense = 0.0
    category_expense = {}
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            if data[0].startswith(current_month):
                amount = float(data[1])
                category = data[2]
                total_expense += amount
                if category in category_expense:
                    category_expense[category] += amount
                else:
                    category_expense[category] = amount
    summary_text = f'Total expense for {current_month}: {total_expense}\n'
    for category, amount in category_expense.items():
        summary_text += f'{category}: {amount}\n'
    messagebox.showinfo("Monthly Summary", summary_text)

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")

# Initialize the file
initialize_file()

# Layout
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Buttons
add_expense_button = tk.Button(frame, text="Add Expense", command=lambda: add_expense(add_date_entry.get(), add_amount_entry.get(), add_category_entry.get(), add_description_entry.get()))
add_expense_button.grid(row=0, column=0, pady=5)

view_expenses_button = tk.Button(frame, text="View Expenses", command=view_expenses)
view_expenses_button.grid(row=1, column=0, pady=5)

filter_expenses_button = tk.Button(frame, text="Filter Expenses", command=filter_expenses)
filter_expenses_button.grid(row=2, column=0, pady=5)

delete_expense_button = tk.Button(frame, text="Delete Expense", command=delete_expense)
delete_expense_button.grid(row=3, column=0, pady=5)

monthly_summary_button = tk.Button(frame, text="Monthly Summary", command=monthly_summary)
monthly_summary_button.grid(row=4, column=0, pady=5)

# Add Expense Entry Fields
add_date_label = tk.Label(frame, text="Date (yyyy-mm-dd):")
add_date_label.grid(row=0, column=1)
add_date_entry = tk.Entry(frame)
add_date_entry.grid(row=0, column=2)

add_amount_label = tk.Label(frame, text="Amount:")
add_amount_label.grid(row=1, column=1)
add_amount_entry = tk.Entry(frame)
add_amount_entry.grid(row=1, column=2)

add_category_label = tk.Label(frame, text="Category:")
add_category_label.grid(row=2, column=1)
add_category_entry = tk.Entry(frame)
add_category_entry.grid(row=2, column=2)

add_description_label = tk.Label(frame, text="Description:")
add_description_label.grid(row=3, column=1)
add_description_entry = tk.Entry(frame)
add_description_entry.grid(row=3, column=2)

# Filter Expenses Entry Fields
filter_by_var = tk.StringVar(value="date")
filter_by_label = tk.Label(frame, text="Filter by:")
filter_by_label.grid(row=5, column=1)
filter_by_menu = tk.OptionMenu(frame, filter_by_var, "date", "category")
filter_by_menu.grid(row=5, column=2)

filter_value_label = tk.Label(frame, text="Filter value:")
filter_value_label.grid(row=6, column=1)
filter_value_entry = tk.Entry(frame)
filter_value_entry.grid(row=6, column=2)

# Delete Expense Entry Fields
delete_date_label = tk.Label(frame, text="Date (yyyy-mm-dd):")
delete_date_label.grid(row=7, column=1)
delete_date_entry = tk.Entry(frame)
delete_date_entry.grid(row=7, column=2)

delete_amount_label = tk.Label(frame, text="Amount:")
delete_amount_label.grid(row=8, column=1)
delete_amount_entry = tk.Entry(frame)
delete_amount_entry.grid(row=8, column=2)

delete_category_label = tk.Label(frame, text="Category:")
delete_category_label.grid(row=9, column=1)
delete_category_entry = tk.Entry(frame)
delete_category_entry.grid(row=9, column=2)

delete_description_label = tk.Label(frame, text="Description:")
delete_description_label.grid(row=10, column=1)
delete_description_entry = tk.Entry(frame)
delete_description_entry.grid(row=10, column=2)

# Expenses display
expenses_text = tk.Text(frame, width=60, height=15)
expenses_text.grid(row=11, column=0, columnspan=3, pady=10)

root.mainloop()