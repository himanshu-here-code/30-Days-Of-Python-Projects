import sqlite3

con = sqlite3.connect("Student Roster DB/Roster.db")
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students( 
          id INTEGER PRIMARY KEY,
          name TEXT,
          age INTEGER,
          grade TEXT
          )''')
con.commit()

while True:
    print("---------student portal---------")
    s_name = str(input("Enter Student's name (or 'quit' to exit): "))
    
    # Exit condition
    if s_name.lower() == 'quit':
        break
    
    try:
        s_age = int(input("Enter student's age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        continue
    
    s_grade = input("Enter student's grade: ")
    
    # Use cursor for INSERT (fixed)
    c.execute("INSERT INTO students (name, age, grade) VALUES (?,?,?)", (s_name, s_age, s_grade))
    con.commit()
    print("Student added successfully!\n")

con.close()