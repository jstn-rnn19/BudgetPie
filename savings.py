import os as os
import datetime as date
import csv as csv

data_money = "Money.csv"

def main ():
    while True:
        print( "========================" )
        print("welcome to BudgetPie")
        print( "========================" )
        print("1. Enter Money")
        print("2. Display Needs")
        print("3. Display Wants")
        print("4. Display Savings")
        print("5. Exit")
        print( "========================" )
        enter_choice = input("Enter your choice: ")


        try:
            if enter_choice == '1':
                adding_all = float(input("Enter how much money: "))
                add_money(adding_all, data_money)
            elif enter_choice == '2':
                print("mas pogi ako")
            elif enter_choice == '3':
                print("pinaka pogi ako")
            elif enter_choice == '4':
                print("pinaka pinaka pogi ako")
            elif enter_choice == '5':
                break
            else:
                print("Out of Range of Choice")
        finally:
            print("Program Execute Successfully")


def add_money(money, file, datenow=None):
    fieldnames = ["Number","Amount", "Needs", "Wants","Savings", "Date"]
    rows = []
    needs = money * .5
    wants = money * .3
    savings = money * .2
    date = datenow.datetime.now().isoformat( " ", "seconds" )
    try:
        if os.path.exists(file):
            with open( file, 'r', newline='' ) as f:
                reader =csv.DictReader(f)
                rows = list(reader)

        new_num = str( len( rows ) + 1 )
        new_row = {
            "Number": new_num,
            "Amount": money,
            "Needs": needs,
            "Wants": wants,
            "Savings": savings,
            "Date": date
        }
        rows.append( new_row )

        with open( file, mode="w", newline="" ) as f:
            writer = csv.DictWriter( f, fieldnames=fieldnames )
            writer.writeheader()
            writer.writerows( rows )

        print(f"Money added successfully to BudgetPie: Total Money Added {money}, {needs} to Needs, {wants} to Wants, and {savings} to Savings in this date {date}")


    except FileNotFoundError:
        print("file not found")



def display_saving():
    pass





if __name__ == "__main__":
    main()