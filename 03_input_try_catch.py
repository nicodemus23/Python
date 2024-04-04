#num = input
#print(num)


try:
    print("Welcome to addition\n") 
    n1 = int(input("Enter first number: ")) 
    n2 = int(input("Enter second number: ")) 
    print(f"The added number is: {n1+n2}") 
except:
    print("Please enter a valid number") #this will be printed if the user enters a non-integer value