#import module
import os
import shutil
import time

def start():
    try:
        print("===============")
        path = input("Enter the path: ")
        files = os.listdir(path)
    except Exception as e:
        print(f"Something went wrong at: {e}")
        return

    print("=============")
    print("Current Path: ", path)
    print("=========================")
    path_parts = path.replace("/", " ").split()
    print(f"Current Work Directories: /{path_parts[-1]}")
    print("==============")
    print("Current Files:")
    print("==============")
    for index, value in enumerate(files, start=1):
        print(f"{index}. {value.lstrip('.')}")
    try:
        user_input = int(input("(0)Quit/(1)Start: "))
        if user_input == 1:
            for file in files:
                filename,extension = os.path.splitext(file)
                extension = extension[1:]
                if os.path.exists(path+"/"+extension):
                    shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
                else:
                    os.makedirs(path+"/"+extension)
                    shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
        elif user_input == 0:
            print("quit from program")
            exit()
    except ValueError as e:
        print(f"Something went wrong at: {e}")


start()
