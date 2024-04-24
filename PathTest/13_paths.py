from pathlib import Path
import os

strNewFileName = "newchild.txt" # New file name
strParentFolder = "parentfolder" # Parent folder
strChildFolder = "childfolder" # Child folder

if not os.path.isdir(strParentFolder): # Check if parent folder exists and if not create it
    os.makedirs(strParentFolder) # Create parent folder
    
if not os.path.isdir(strChildFolder): # Check if child folder exists and if not create it
    os.makedirs(strChildFolder) # Create child folder
    
