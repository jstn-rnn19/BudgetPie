import os as os
import json as json

# def display_data (file):
#     found = True
#
#     try:
#         if os.path.exists(file):
#             with open( file, "r" ) as f:
#                 data = json.load( f )
#         for id, info in data.items():
#             print(f"{id} {info}")
#             found = True
#         if not found:
#             print( "No Save Data." )
#
#     except (FileNotFoundError, json.JSONDecodeError):
#         print("Error")


class Users:
    amount = 0.00
    num_of_user = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.username = first + '_' + last
        Users.amount =+ 1



    def full_name(self):
        return "{} {}".format(self.first,self.last)

    def create_file_by_name(self):
        file_path = f"users/{self.username}"
        if not os.path.exists( file_path ):
            os.makedirs(file_path)
            print("File path Created Successfully")
            print( f"Your Username is {self.username}" )
        else:
            print("File already Exist")

    @classmethod
    def check_username(cls, old_user):
        file_path = f"users/{old_user}.json"
        if os.path.exists(file_path):
            print("pogi ko")
            return True
        return False