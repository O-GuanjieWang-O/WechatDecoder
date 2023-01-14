from itertools import count
import os
import shutil

source_folder =input("Enter source folder: ")
destination_folder = input("Enter destination folder: ")
function=int(input("Input the number to perform op:\n 1. move \n 2. copy\n"))

def copy(source,destination_folder):
    for file_name in os.listdir(source):
         print(file_name)
         temp = source +"\\"+file_name
         print(temp)
         dest = destination_folder + "\\"+file_name
         print(dest)
         if os.path.isfile(temp):
             shutil.copyfile(temp, dest)
             print('copyfile:', file_name +" to "+destination_folder)
         else:
             copy(temp,destination_folder)

def move(source,destination_folder):
    for file_name in os.listdir(source):
         print(file_name)
         temp = source +"\\"+file_name
         print(temp)
         dest = destination_folder + "\\"+file_name
         print(dest)
         if os.path.isfile(temp):
             shutil.move(temp, dest)
             print('move:', file_name +" to "+destination_folder)
         else:
             move(temp,destination_folder)

def main():
    if(function==1):
        move(source_folder,destination_folder)
    elif(function==2):
        copy(source_folder,destination_folder)


if __name__ == "__main__":
    main()
   