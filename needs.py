import json as json
import os as os
import utils as utility

def add_need(user: utility.Users):
    file_path = "users/Jusrine_Sanidad/wants_data.json"
    try:
        if not os.path.exists(file_path):
            with open( file_path, "r" ) as f:
                try:
                    info = json.load( f )
                except json.JSONDecodeError:
                    info = {}
    except FileNotFoundError:
        print("Does not Exist")
        info = {}

        info = {"UserName": user.username, "First Name": user.first, "Last Name": user.last, "Amount": user.amount}


        with open( file_path, 'w' ) as f:
             json.dump(info, f ,indent=4)
