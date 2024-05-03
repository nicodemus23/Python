#Loops
#Python has 2 primitive loops
#While & For

#While loop
i = 0
while(i < 6):
    #print(i)
    i += 1 #increment i by 1

#break while
i = 0
while(i < 6):
    #print(i)
    i += 1
    if i == 3:
        break #stop at 3
    i += 1
    
#continue while
i = 0
while(i < 6):
    i += 1
    if i == 3:
        continue #skip 3
    #print(i) #print 1, 2, 4, 5, 6
    
#else
i = 0
while(i < 6):
    #print(i)
    i += 1
else:
    #print("i is no longer less than 6")
    pass #pass is a null statement that does nothing (acts as a placeholder for an empty else body since there's an error without)
    
#For loop
something = "pen", "sun", "moon"

for thing in something:
    #print(thing)
    pass
    
for i in "moon":
    #print(i)
    pass
    
for i in range(6):
    #print(i)
    pass
    
for i in range(2, 6):
    #print(i)
    pass

for i in range(len(something)):
    #print(something) #print ('pen', 'sun', 'moon')
    pass
    
for i in range(len(something)):
    #print(something[i]) 
    pass
    
for i in range(6):
    #print(i)
    pass
    
for i in range(2, 6):
    #print(i)
    pass
    
for i in range(2, 6, 10):
    #print(i)
    pass

#reverse loop
for i in reversed(range(6)):
    print(i)
    
#nested for loop
everything = ["pen", "sun", "moon"]

for a in something:
    for b in everything:
        print(a, b)