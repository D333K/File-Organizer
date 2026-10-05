import os
import pyfiglet
import termcolor
from operations import *

print("Enter The Full Directory Name For Start Organizer:-")
dir_name = input("Directory name: ").strip()

if not dir_name:
    print("Please Enter The Full Path To Start Work!")
    exit()

if not os.path.exists(dir_name):
    print("Please Enter Correct Path To Start Work!")
    exit()

# duplicate_counter = 0
move_counter = 0 # How many files has moved successfully.

for root, dirs, files in os.walk(dir_name):
   
    for name in files:

        file_path = os.path.join(root, name)

        type = where_put_it(name)

        folder_path = os.path.join(root, type)

        os.makedirs(folder_path, exist_ok=True)

        file_move_path = os.path.join(folder_path, name)

        if os.path.exists(file_move_path):
            counter = 1
            old_name, exten = os.path.splitext(name)

            while os.path.exists(file_move_path):
                new_name = f"{old_name}_{counter}{exten}"
                file_move_path = os.path.join(folder_path, new_name)
                counter += 1

        os.rename(file_path, file_move_path)
        move_counter += 1

        print("Please Wait...")
        print('-' *20)
        print(f"Moved {name} => {type}")
        print('-' *20)

    break

print("Organized Successfully")
print(f"{move_counter} Files Has Moved")
print()
input("Press To Countinue'")
print(termcolor.colored(pyfiglet.figlet_format("Dark Knight"), color="black"))