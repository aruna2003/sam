import tkinter as tk

def check_expense():
    
    expense = int(expense_entry.get())
    test_values = [1,2,89, 90, 91,45]
    
            

    if expense in test_values:
        message_label.config(text="Error: Is in Boundary value.")
        
    elif expense > 90:
        message_label.config(text="Error: Expense is too high!")
    elif expense < 90:
        message_label.config(text="Success: Expense is within the limit.")
    else:
        message_label.config(text="Wonderful: Expense is exactly $90!")


app = tk.Tk()
app.title("Expense Checker")


expense_label = tk.Label(app, text="Enter Expense:")
expense_label.pack()
expense_entry = tk.Entry(app)
expense_entry.pack()


check_button = tk.Button(app, text="Check", command=check_expense)
check_button.pack()


message_label = tk.Label(app, text="")
message_label.pack()


app.mainloop()
