import sys

args_lower = [item.lower() for item in sys.argv]

#print("3rd parameter: " + args_lower[2])
my_list = ['Wade', 'Wilson', 'Sarah']

if '--help' in args_lower:
    print("""
          This is your help system:
          use the following comand arguments:
          
          --help (display this help/all valid arguments)
          --1 (show list)
          --a (add value to list)
          """)
    
elif '--1' in args_lower: # 
    print(my_list) 
else:
    if args_lower.count('--a'): # 
        a_index = args_lower.index('--a') 
        if a_index + 1 < len(sys.arg):
            print("a_index: " + str(a_index))
            a_value = sys.argv[a_index + 1]
            print("a_value: " + str(a_value))
            my_list.append(a_value)
            print(my_list)
        else:
            print("No value provided for --a argument")
    elif args_lower.count('--r'): # remove value from list
        r_index = args_lower.index('--r') # get index of --r argument
        if r_index + 1 < len(sys.arg): # check if there is a value after --r argument
            print("r_index: " + str(r_index)) # print index of --r argument
            r_value = sys.argv[r_index + 1] # get value after --r argument
            if r_value in my_list: # check if value is in list
                my_list.remove(r_value) # remove value from list
                print(my_list) # print updated list
            else:
                print("Value not found in list")
        else:
            print("No value provided for --r argument")
            
    
        
        
        
#     elif '--1' in args_lower:
#     print(my_list)
# else:
#     if args_lower.count('--a'):
#         a_index = args_lower.index('--a')
#         print("a_index: " + str(a_index))
#         a_value = sys.argv[a_index + 1]
#         print("a_value: " + str(a_value))
#         my_list.append(a_value)
#         print(my_list)
#     else:
#         print("No value provided for --a argument")
