import os
import shutil

my_dir = os.getcwd()
things = os.listdir(my_dir)

for x in things:
    if "." in x[0]:
        pass
    else:
        shutil.move(my_dir+"/"+x, my_dir+"/"+"."+x)

print("The Files Has Rename.")
