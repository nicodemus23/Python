#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#Dictionaries are ordered, changeable, don't allow duplicates, and written with curly braces.

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1966
}
print(dict1) #print the dictionary

print(dict1["brand"]) #print the value of the key "brand"   

dict1["model"] = "Thunderbird" #change the value of the key "model"
print(dict1) 

dict1["newKey"] = "Chevrolet" #add a new key-value pair to the dictionary
print(dict1)

print(len(dict1)) #print the length of the dictionary
#each key-value pair counts as one item

dict2 = {
    "street": "143 Main Street",
    "city": "Los Angeles",
    "city": "Sale Lake City" #duplicate key - last value passed is what gets assigned to the key
}

print(dict2)

#dictionary constructor
dict3 = dict()
dict3["name"] = "Alberto"
dict3["age"] = 25

print(dict3)

#dictionairy can hold lists, tuples, sets, dictionaries, etc.
#nested dictionaries are allowed
dict4 = {
    'fruits': ('mango', 'strawberry', 'tangerine', 'orange'),
    'speed': (10, 20, 30, 40, 50),
    'pokemon': {"type": 'grass', "name": 'Bulbasaur', "HP": 200}
}

#number as keys
dict5 = {
    1: "one",
    2: "two",
    3: "three"
}   

print(dict5[2]) #print the value of the key 2