from itertools import count
import os
import shutil

function=int(input("Input the number to perform op:\n 1. move \n 2. copy\n 3. moveLivp\n 4. moveHeic\n 5.livpToReadable\n"))
if function != 5 :
    source_folder =input("Enter source folder: ")
    destination_folder = input("Enter destination folder: ")
else: 
    source_folder =input("Enter source folder: ")

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

def moveLivp(source,destination_folder):
    for file_name in os.listdir(source):
         if file_name.find("livp") != -1:
            print(file_name)
            temp = source +"\\"+file_name
            print(temp)
            dest = destination_folder + "\\"+file_name
            print(dest)
            if os.path.isfile(temp):
                shutil.move(temp, dest)
                print('copyfile:', file_name +" to "+destination_folder)
            else:
                move(temp,destination_folder)

def livpToReadable(source):
     for file_name in os.listdir(source):
         if file_name.find("livp") != -1:
            temp = source +"\\"+file_name
            print("7z x "+ "\""+temp+"\"" +" -o"+source)
            convert = lambda:os.system("7z x "+ "\""+temp+"\"" +" -o"+source)
            convert()
            delLivp = lambda:os.system("del "+"\""+temp+"\"")
            delLivp()
            
               



def moveHeic(source,destination_folder):
    for file_name in os.listdir(source):
         if file_name.find("heic") != -1:
            print(file_name)
            temp = source +"\\"+file_name
            print(temp)
            dest = destination_folder + "\\"+file_name
            print(dest)
            if os.path.isfile(temp):
                shutil.move(temp, dest)
                print('copyfile:', file_name +" to "+destination_folder)
            else:
                move(temp,destination_folder)

def main():
    if(function==1):
        move(source_folder,destination_folder)
    elif(function==2):
        copy(source_folder,destination_folder)
    elif(function==3):
        moveLivp(source_folder,destination_folder)
    elif(function==4):
        moveHeic(source_folder,destination_folder)
    elif(function==5):
        livpToReadable(source_folder)
    
    


if __name__ == "__main__":
    main()
   