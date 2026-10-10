import json
from datetime import datetime, date
def load_expenses():
    try:
        with open("expenses.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
        
expenses=load_expenses()

def save_expenses(expenses):
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)
    

def get_amount():
    while True:
        try:
            amount = int(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Enter again.")


def get_category():
    while True:
        category = input("Enter category: ").strip()

        if category == "":
            print("Category cannot be empty.")
        else:
            return category


def get_description():
    while True:
        description = input("Enter description: ").strip()

        if description == "":
            print("Description cannot be empty.")
        else:
            return description


def get_expense_number(expenses):
    while True:
        try:
            expense_number = int(input("Enter expense number: "))

            if 1 <= expense_number <= len(expenses):
                return expense_number - 1
            else:
                print("Invalid expense number. Enter again.")

        except ValueError:
            print("Invalid input. Enter a number.")
            
def display_expenses(expenses):
    for index, expense in enumerate(expenses,start=1):
        print("\nExpense", index)
        print("Amount:", expense["Amount"])
        print("Category:", expense["Category"])
        print("Description:", expense["Description"])
        print("Date:", expense.get("Date", "Not available"))
        
        
def get_date():
    while True:
        date_input = input(
            "Enter date (YYYY-MM-DD) [" + date.today().strftime("%Y-%m-%d") + "]: "
        ).strip()

        if date_input == "":
            return date.today().strftime("%Y-%m-%d")

        try:
            entered_date = datetime.strptime(date_input, "%Y-%m-%d").date()

            if entered_date > date.today():
                print("Date cannot be in the future.")
                continue

            return entered_date.strftime("%Y-%m-%d")

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")



    
    

def show_menu():
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. View Category Summary")
    print("5. Delete Expense")
    print("6. Edit Expense")
    print("7. Exit")
    print("====================================")



def get_choice():
    while True:
        try:
            choice=int(input("Enter your choice:"))
            if 1<=choice<=7:
                return choice
            else:
                print("Choice must be between 1 and 7.")
        except ValueError:
            print("Invalid choice. Enter a number.")

 
def add_expense(expenses):
    amount=get_amount()
    category=get_category()
    description=get_description()
    date = get_date()
    
    expense={
        "Amount": amount,
        "Category": category,
        "Description": description,
        "Date":date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!") 
           
           
           
def delete_expense(expenses):
        print("Delete expense")
        if not expenses:
            print("No expenses found.")
        else:
           display_expenses(expenses)
           index=get_expense_number(expenses)
           expenses.pop(index)
           save_expenses(expenses)
           print("Expense deleted successfully")
           
           
           

def edit_expense(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        display_expenses(expenses)
        index=get_expense_number(expenses)
        new_amount=get_amount()
        new_category=get_category()
        new_description=get_description()
        expenses[index]["Amount"] = new_amount
        expenses[index]["Category"] = new_category
        expenses[index]["Description"] = new_description
        save_expenses(expenses)

        print("Expense updated successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        display_expenses(expenses)

                    
                    
def total_spending(expenses):
            if not expenses:
               print("No expenses found.")
            else:
               total=0
               for expense in expenses:
                total+=expense["Amount"]
               print("Total spending is:",total)
                

def view_category(expenses):
       if not expenses:
        print("No summary found.")
       else:
        summary = {}

        for expense in expenses:
            category = expense["Category"]

            if category in summary:
                summary[category] += expense["Amount"]
            else:
                summary[category] = expense["Amount"]

        for category, amount in summary.items():
            print(category, ":", amount)


while True:
    show_menu()
    choice=get_choice()




    if(choice==1):
        add_expense(expenses)



    elif(choice==2):
        view_expenses(expenses)
  



    elif(choice==3):
        total_spending(expenses)



        
    elif(choice==4):
        view_category(expenses)



    elif(choice==5):
        delete_expense(expenses)

 
    
    elif(choice==6):
            edit_expense(expenses)

            
    elif(choice==7):
        print("Exit.")
        break