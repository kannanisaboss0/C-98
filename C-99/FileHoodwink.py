
import random
import os
path=os.getcwd()
print(path)
File1=input("Enter the first file's name:")
File2=input("Enter the second file's name:")

def ReadDatafromFiles(file1,file2) :
    openFile1=open(file1,"r+")
    readFile1=openFile1.read()
    openFile1.close()
    openFile2=open(file2,"r+")
    readFile2=openFile2.read()
    openFile2.close()
    openFile1=open(file1,"w+")
    openFile1.write(readFile2)
    openFile2=open(file2,"w+")
    openFile2.write(readFile1)
    print("Data in the stipulated files has been replaced. Please check")
    print("Thank you for using FileHoodwink.py")

           
    
    
   
    
    
    
if(os.path.exists(path+"/"+File1)):
    if(os.path.exists(path+"/"+File2)):
        ReadDatafromFiles(File1,File2)
    else:
        print("Could not find the file:"+File2)
        yes= input("Create a new file for labeled:"+File2+".Type 'Yes' if you want to, and 'No' if you don't wnat to")  
        if(yes=="Yes"):
            File2=open(File2,"a+")
            print("File created")
            print("Thank you for using FileHoodwink.py")
        else:
            print("Request accepted")
            print("Thank you for using FileHoodwink.py")
               
else:
    print("Could not find the file:"+File1)
    yes= input("Create a new file for labeled:"+File1+". Type 'Yes' if you want to, and 'No' if you don't want to:")  
    if(yes=="Yes"):
        File1=open(File1,"a+")
        print("File created")
        print("Thank you for using FileHoodwink.py")
        
    else:
        print("Request accepted")
        print("Thank you for using FileHoodwink.py")









