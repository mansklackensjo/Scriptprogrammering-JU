# Create a program that asks the user to enter a path to a directory on the file system. 
# Your program should then check if that directory only contains files with the following names:

#     config.xml
#     backup-config-YYYY-MM-DD.xml

# There may exists several files with the name backup-config-YYYY-MM-DD.xml, and YYYY-MM-DD should of 
# course be a date for when the backup of the config.xml was created (e.g. 2018-11-12). 
# Your program should print text telling the user if all the files were named in one of these two 
# formats, or if there exist files that doesn't follow these formats (in which case you should
# print the name of these files that don't follow the formats).

# C:\Users\Måns\Desktop\Scriptprogrammering-JU\4.5_right_format
import os
import re

def check_files(directory_path):
    if os.path.isdir(directory_path) == True:

        files = os.listdir(directory_path)

        backup_pattern = r"backup-config-\d{4}-\d{2}-\d{2}\.xml"
        invalid_files = []


        for file in files:
            if file == "config.xml":
                continue

            elif not re.match(backup_pattern, file):
                invalid_files.append(file)

        
        if invalid_files:
            print("The following files don't follow the correct formats:")
            for file in invalid_files:
                print(file)
        else:
            print("All files follow the formats.")

    else:
        print(f"{directory_path} is not an existing path.")

    

directory_path = input("Enter a path to a directory: ")
check_files(directory_path)