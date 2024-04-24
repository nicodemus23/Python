#.isdir - check if folder exists at current directory 
#.makedirs - create folder at current directory
#.chdir - change default directory to folder
#.isfile - check if file exists at current directory
#.getcwd - get current working directory (returns path)
#.listdir - returns list of contents in current directory
#.endswith - string function that checks if file name ends with a certain string (defined in the function)


from pathlib import Path
import os

strNewFileName = "newchild.txt" # New file name
strParentFolder = "parentfolder" # Parent folder
strChildFolder = "childfolder" # Child folder

if not os.path.isdir(strParentFolder): # Check if parent folder exists and if not create it
    os.makedirs(strParentFolder) # Create parent folder
    
if not os.path.isdir(strChildFolder): # Check if child folder exists and if not create it
    os.makedirs(strChildFolder) # Create child folder
    
os.chdir(strChildFolder) # Change directory to child folder

if not os.path.isfile(strNewFileName): # Check if file exists and if not create it
    print(os.getcwd()) # Print current working directory
    file = open(os.getcwd() + "\\" + strNewFileName, "w") # Create new file in child folder
    file.write("new file created") # Write to file
    file.close() # Close file
    
for f in os.listdir(): # Loop through files in current directory
    if f.endswith(".txt"): # Check if file is a text file
        strCurrentPath = os.getcwd() 
        strParentPath = str(Path(strCurrentPath).parents[0]) # Get parent path based on current path (takes a level up)
        strSavePath = f'{strParentPath}\\' + strParentFolder + "\\" + strNewFileName # concatenate parent path with parent folder and new file name 
        
        file = open(strSavePath, 'w') # Create new file in parent folder
        file.write("another new file created") # Write to file
        file.close()  
        