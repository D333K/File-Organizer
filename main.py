import os
from operations import *

print("Enter The Full Directory Name For Start Organizer:-")
dir_name = input("Directory name: ")

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
        os.system("cls" if os.name == "nt" else "clear")

    break

print("Organized Successfully")
print(f"Moved {move_counter}")