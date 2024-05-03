#File IO
# 'w' - write   Stream position at the beginning of the file and create a new file if it does not exist
                # if the file exists, clear the file and write to it
# 'r' - read    Stream position to the BEGINNING of the file and create a new file if it does not exist
# 'a' - append  Stream position to the END of the file and create a new file if it does not exist

# 'w+' - write and read - if file exists, wipe out the content and write to it
# 'r+' - read and write - Stream position to the beginning of the file and create a new file if it does not exist
# 'a+' - read, write and append - Stream position to the end of the file and create a new file if it does not exist

#write to a file
file = open('text1.txt', 'w') #makes file accessible inside code
file.write("Hello, this is a test file.\n")
file.write("This is the second line.\n")
file.close() #closes the file

#read from a file and print the content to the console
file = open('text1.txt', 'r') 
content = file.read()
file.close()

print(content)

#append to the file
file = open('text1.txt', 'a') 
file.write("Adding this via append.\n")
file.close()

#open file using 'with' statement ("w" will create a new file or overwrite an existing file with the same name)
with open("text1.txt", "w") as file: #open file and assign it to variable 'file' using 'with' statement and write to it 
    file.write("This is a test file using 'with' statement.\n") #no need to close the file as 'with' does it automatically
    
#open file using 'with' statement ("r" will open an existing file for reading)
with open("text1.txt", "r") as file: #open file and assign it to variable 'file' using 'with' statement and read from it
    content = file.read() #read the content of the file
    print(content) #print the content to the console
    
#open file using 'with' statement ("a" will open an existing file for appending)
with open("text1.txt", "a") as file: #open file and assign it to variable 'file' using 'with' statement and append to it
    file.write("Adding this via append using 'with' statement.\n") #no need to close the file as 'with' does it automatically
    

    
    
