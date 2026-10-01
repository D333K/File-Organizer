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

        category_folder = os.path.join(root, where_put_it(file_path))

        category_folder_path = os.path.join(category_folder, name)

        os.makedirs(category_folder, exist_ok=True)

        if os.path.exists(category_folder_path): # Change file name if it's already exists.
            # duplicate_counter = 1
            
            file_name, file_exten = os.path.splitext(category_folder_path)
            
            category_folder_path = f"{file_name}_1{file_exten}"

        os.rename(file_path, category_folder_path)
        move_counter += 1

        print("Please Wait...")
        print('-' *20)
        print(f"Moved {name} => {where_put_it(file_path)}")
        print('-' *20)

    break

print("Organized Successfully")
print(f"{move_counter} Files Has Moved")
print()
print(termcolor.colored(pyfiglet.figlet_format("Dark Knight"), color="black"))