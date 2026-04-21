expenses = []

print("Welcome to Expense Tracker")

while True:
    print ("Menu")
    print("press 1 to Add Expense")
    print("press 2 to view ")
    print ("press 3 to see total expense")
    print("press to 4 to Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        date = input("Enter data of expense")
        category = input("Enter what kind of expense you did")
        description = input("describe about what product you purchase")
        Amount = float(input("Enter your amout you expend"))

        expense = {
            "date": date,
            "category":category,
            "description": description,
            "amount":Amount

        }
        expenses.append(expense)
        print("Expense Added successfully")
    elif choice == 2:
        if(len(expenses) == 0):
            print("There is not expenses list")
        else:
            print("This is list of Expenses")
            count = 1
            for exp in expenses:
                print(f" Expenses Number {count} -> {exp["date"]},{exp["category"]},{exp["description"]},{exp["amount"]} ")
                count += 1
    elif choice == 3:
        total = 0
        for ex in expenses:
            total = total + ex['amount']
        print(f"the total expense is {total}")
    elif choice == 4:
        print("Thank you for using our system")
        break
    else:
        print("invalid choice")
    