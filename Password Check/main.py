import time
from getpass import getpass

password = "0000"

attemps = 0
attemps_limit = 3


while attemps < attemps_limit:
    attemps += 1
    user_input = getpass("password: ")
    if user_input == password:
            print("correct")
            break
    else:
            time.sleep(1) 
            print("incorrect.. Try again")