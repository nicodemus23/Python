import random as rd

print(rd.random()) #returns a random float number between 0 and 1

print(rd.uniform(10, 20)) #returns a random float number between 10 and 20 (or any two numbers you specify)

print(rd.randint(0, 2)) #returns a random integer between 0 and 2 (or any two numbers you specify) also includes the last number

print(rd.randrange(0, 100, 2)) #returns a random integer between 0 and 10 in steps (2) but the last number is excluded (0, 2, 4, 6, 8, 10) 

print(rd.choice([1, 2, 3, 4, 5])) #returns a random element from the list

print(rd.choices([1, 2, 3, 4, 5], k=3) ) #returns a list of random elements from the list with the specified length of numbers to return

my_list = [1, 2, 3, 4, 5]
rd.shuffle(my_list) #shuffles the list
print(my_list)

#define a sample size of how many elements you want to return from a collection of elements
print(rd.sample([1, 2, 3, 4, 5], k=3) ) #returns a list of random elements from the list with the specified length of numbers to return but does not shuffle the list
rd.sample((my_list), k=3) #returns a list of random elements from the list with the specified length of numbers to return but does not shuffle the list
print(my_list)