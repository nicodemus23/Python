# my_module.py

def greet(name): # method 
    print(f"Hello, {name}!") 

class Person: 
    def __init__(self, name): # constructor 
        self.name = name # set name attribute

    def say_hello(self): # method
        print(f"Hello, my name is {self.name}!") 
        
    def __str__(self): # method 
        return f"Person({self.name})" 
    
    def __repr__(self): # method
        return f"Person({self.name})"
    
    def __eq__(self, other): # method
        return self.name == other.name
    
    def __ne__(self, other): # method
        return self.name != other.name
    
    def __lt__(self, other): # method
        return self.name < other.name
    
    def __le__(self, other): # method
        return self.name <= other.name
    
    def __gt__(self, other): # method
        return self.name > other.name
    
    def __ge__(self, other): # method
        return self.name >= other.name