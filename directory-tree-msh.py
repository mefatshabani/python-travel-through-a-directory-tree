#Python Program by Mefat Shabani

import os
from pathlib import Path
#Recursive function to check directory tree and all files inside
def check_directory_tree(directory,files_inside):
    print(files_inside,Path(directory).name)
    files_inside+= "----"
    file_names = []
    directory_names = []
    for value in os.listdir(directory):
        if os.path.isfile(directory + os.path.sep + value):
            file_names.append(value)
        else:
            directory_names.append(value)
    #This for loop perform second task so it lists all stats that are related to the file
    for file_name in file_names:
        print(files_inside,file_name,Path(directory + os.path.sep + file_name).stat())
    for subdirectory in directory_names:
        check_directory_tree(directory+os.path.sep+subdirectory,files_inside)
check_directory_tree(".","") 

