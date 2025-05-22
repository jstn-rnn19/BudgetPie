import utils as utility
import os as os
def main ():
    while True:
        print( "========================" )
        print( "welcome to BudgetPie" )
        print( "========================" )
        user = input( "Are you a New User?(Y/N): " ).lower()
        print( "========================" )
        if user == 'y':
            print( "Sign Up to BudgetPie" )
            print( "========================" )
            fname = input( "Enter your First Name: " ).capitalize()
            print( "================" )
            lname = input( "Enter your Last Name; " ).capitalize()
            print( "================" )
            print( "Creating Username......." )
            user = utility.Users( fname, lname )
            file_path = user.create_file_by_name()
            print( f"{file_path}" )



        elif user == 'n':
            old_user = input( "Enter username to verify: " )

            if utility.Users.check_username(old_user):
                name = old_user.full_name()
                while True:
                    print( "========================" )
                    print( f"welcome back {name} to BudgetPie" )
                    print( "========================" )
                    print( "1. Enter Money" )
                    print( "2. Display Needs" )
                    print( "3. Display Wants" )
                    print( "4. Display Savings" )
                    print( "5. Exit" )
                    print( "========================" )
                    enter_choice = input( "Enter your choice: " )

                    try:
                        if enter_choice == '1':
                            adding_all = float( input( "Enter how much money: " ) )

                        elif enter_choice == '2':
                            print( "mas pogi ako" )
                        elif enter_choice == '3':
                            print( "pinaka pogi ako" )
                        elif enter_choice == '4':
                            print( "pinaka pinaka pogi ako" )
                        elif enter_choice == '5':
                            break
                        else:
                            print( "Out of Range of Choice" )
                    finally:
                        print( "Program Execute Successfully" )
            else:
                print( "User not Exist" )
        else:
            print( "Invalid Input" )


if __name__ == "__main__":
        main()