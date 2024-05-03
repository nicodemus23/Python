#JSON
#Java Script Object Notation
#It is a lightweight data interchange format
#Often used when data is sent from a web API to a client

#key-value pairs
#data is separated by commas
#curly braces hold objects (key-value pairs or dictionaries)
#square brackets hold arrays
#strings are in double quotes
#numbers are not in quotes
#booleans are not in quotes

#Example:
{
    "employees":[ 
        {"name": "John",
        "age": 30,
        "city": "New York"}
        ]
}

import json

#string
data = '{"name": "John", "age": 30, "city": "New York"}' #JSON data
print(data) #print JSON data

#convert string json
json_data = json.loads(data) #parse JSON data into a Python dictionary / converts string to json
print(json_data) #print the Python dictionary

#convert json back to a string
strjson = json.dumps(json_data) #converts json to string
print(strjson) #print the string


names = [
    {
        "name:": "John",
        "age": 30,
        "city": "New York",
        "married": True
    },
    {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles",
        "married": False
    },
    {
        "name": "Jake",
        "age": 35,
        "city": "Chicago",
        "married": True
    }
]

#write json to file
with open('names.txt', 'w') as file:
    file.write(json.dumps(names, indent=4)) #write the json data to the file with indentation

with open('names.txt', 'r') as file:
    all_names = json.loads(file.read()) #read the json data from the file and assign it to a variable
    
print(all_names[1]['age']) #print the age of the second person in the list






