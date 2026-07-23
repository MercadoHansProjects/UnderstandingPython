##Expense Tracker

import csv


while True:
    print("Another day, Another expense, no?") 
    action = input("Pick one! 'add', 'view', 'clear', 'exit': ")
    if action == "add":
         category = input("Enter type of expense: ")
         description = input("Enter description: ")
         amount = float(input("Enter amount: "))
         with open("expenses.csv", "a", newline="") as file:
              writer = csv.writer(file)
              writer.writerow([category, description, amount])
         print("Expenses Saved!")
    elif action == "view":
         with open("expenses.csv", "r") as file:
              reader = csv.reader(file)
              for row in reader:
                   print(row)
    elif action == "clear":
         with open("expenses.csv", "w", newline="") as file:
              pass
    elif action == "exit":
         break
    





    




