#Sets
#Used to store multiple items in the same variable (like lists, tuples, dictionaries and arrays)
#A collection that is unordered, unindexed and have no duplicate values

set1 = {"red", "blue", "green", "yellow", "orange", "purple"} #create a set
print(set1) #print the set

#doesn't store values in order. Just stores them 

set2 = {"red", "blue", "green", "yellow", "orange", "purple", "green"} #create a set with duplicate values
print(len(set2)) #print the length of the set (it ignores the duplicate value)
print(set2) #print the set (it ignores the duplicate value)

#multiple data types
set3 = {"Robbie", "Judy", True, 25, 5.66}
print(set3) 

#set constructor
set4 = set((1,2,3,4,5,6,5,4,3,2,1)) #create a set using the set constructor / ignores duplicate values
print(set4) 

set5 = set("Hello my name is Alberto Gonzales") #create a set from a string 
print(set5) 

#set operations
setA = set(("1234567"))
setB = set(("123489"))
setC = set(("123"))

#union
print(setA.union(setB)) #combine two sets

#intersection - returns what's common between two sets
print(setA.intersection(setB)) #print the common values between two sets

#superset - returns true if all items in the set are present in the specified set
print(setA.issuperset(setB)) #check if setA is a superset of setB
print(setA.issuperset(setC)) #check if setA is a superset of setC
print(setC.issuperset(setA)) #check if setC is a superset of setA

#difference - returns the difference between two sets
print(setA.difference(setB)) #print the difference between two sets
print(setA - setB) #print the difference between two sets

