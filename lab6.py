#File handling
#Python File Open
#Syntax
f = open("demofile.txt")
f = open("demofile.txt", "rt")
#Python File Open
#Open a File on the Server
demofile.txt

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!

#The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())

#If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

#Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(5))

#Read Lines
f = open("demofile.txt", "r")
print(f.readline())

#By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)

#Close Files
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#Python File Write
#Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#Open the file "demofile3.txt" and overwrite the content:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

#Create a file called "myfile.txt":
f = open("myfile.txt", "x")

#Create a new file if it does not exist:
f = open("myfile.txt", "w")

#Python Delete File
#Remove the file "demofile.txt":
import os
os.remove("demofile.txt")

#Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#To delete an entire folder, use the os.rmdir() method:
import os
os.rmdir("myfolder")










