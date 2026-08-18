import sqlite3

con = sqlite3.connect("finance.db")
c = con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS transactions(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          category TEXT,
          description TEXT,
          amount INTEGER
          )""")
con.commit()

while True:
    print("\n------EXPENSE TRACKER-------")
    print("1: Add a new expense.\n2: View all raw expenses.\n3: View total spending by category (The Analytics Report).\n4: Exit.")
    
    try:
        user_choice = int(input("choose an option(1,2,3,4): "))
        
        if user_choice not in (1,2,3,4):
            print(f"{user_choice} is invalid. choose a number (1,2,3,4)")
            continue
            
        if user_choice == 1:
            print("------ADD AN EXPENSE-----")
            category_ = input("Enter Category : ")
            description_ = input("Enter description: ")
            amount_ = int(input("Enter amount : $"))
            c.execute("INSERT INTO transactions(category , description, amount) VALUES(?,?,?)",(category_, description_,amount_))
            con.commit()
            print("ADDED SUCCESSFULLY")
            
        elif user_choice == 2:
            print("-----VIEW ALL EXPENSES----\n")
            c.execute("SELECT * FROM transactions")
            expenses = c.fetchall()
            for expense in expenses:
                id = expense[0]
                category = expense[1]
                description = expense[2]
                amount = expense[3]
                print(f"{description} : ${amount}")
            
        elif user_choice == 3:
            print("-----TOTAL SPENDING BY CATEGORY-----")
            c.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category;")
            expenses = c.fetchall()
            for expense in expenses:
                category = expense[0]
                amount = expense[1]
                print(f"{category} : ${amount}")
            
        elif user_choice == 4:
            print("Goodbye!")
            break
            
    except ValueError:
        print("Invalid input! Please enter a number.")
        
con.close()