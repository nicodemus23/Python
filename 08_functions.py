#function
def my_function():
  print("Hello from a function")
  
my_function()

#function with return argument
def my_function_returns():
    return "My function has returned"

print(my_function_returns())

#arguments
def my_function2(name, age):
    print(f"Hi {name}! Your age is: {age}")
    
my_function2("John", 36)

#arbitrary arguments
def my_function_arb(*kids): #*args is a convention but you can use any name
    print(f"I have {len(kids)} kids.") 
    print(f"The youngest is {kids[1]}.")  #index is the value instead of keyword
    
my_function_arb("Walter", "Donny", "The Dude")

#keyword arguments
def my_function_keyword(child3, child1, child2):
    print(f"The youngest child is {child3}.")
    
my_function_keyword(child1 = "Walter", child2 = "Donny", child3 = "The Dude")

#arbitrary keyword arguments
def my_function_argKey(**kids): #**kwargs is a convention but you can use any name
    print(f"The youngest child is {kids['child3']}.") #index is the keyword instead of value 
    
my_function_argKey(child1 = "Walter", child2 = "Donny", child3 = "The Dude")

#default parameters
def my_function_def(age=19):
    print(f"My age is {age}.")
    
my_function_def() #default value
my_function_def(36) #passed value

#global variables
x = "awesome"
def myglobal():
    x = "fantastic"
    print("I am " + x)

myglobal() #uses the local variable that's in scope

#recursive function
loops = 0 #global variable
def try_recursion(value):
    global loops #use the global variable outside the function
    loops += 1
    print(f"Looping: {loops}") #print the number of loops
    
    if value > 0:
        result = value + try_recursion(value - 1) #recursive function that calls itself within itself until the value is 0
        print(result)
    else:
        result = 0 #base case
    return result 
    
x = try_recursion(6) #6 + 5 + 4 + 3 + 2 + 1 + 0 = 21
print(x) 

