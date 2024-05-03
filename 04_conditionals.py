
#conditionals
'''
Equal: a == b
Not Equal: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

#if statement
a = 3
b = 2
if a < b:
    print(f"{a} is less than {b}")
elif a > b:
        print(f"{a} is greater than {b}")
else:
        print(f"{a} is equal to {b}")

#ternary operator (conditional expression) - a one-liner if-else statement that assigns a value to a variable based on a condition 
a = 40
b = 39
print(f"{a} is less than {b}") if a < b else print(f"{a} is greater than {b}") if a > b else print(f"{a} is equal to {b}")

#logical operators
a, b, c = 200, 34, 100

if a > b and not c < a: #in python you can use 'and' instead of '&&' and 'or' instead of '||' and 'not' instead of '!' 
    print(f"Both conditions are True")
    
if a != b:
    print(f"{a} is not equal to {b}")
    
#nested if statements
x = 41
if x > 10:
    print(f"{x} is Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
        if x > 20:
            print("above 20")
        else: 
            print("but not above 20")
            
#pass - avoids getting an error because python does not use {} to define code blocks
if a > b:
    pass