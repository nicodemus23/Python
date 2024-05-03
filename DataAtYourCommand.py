import json

def main(): # Define the main function
    #add, list, find, delete, quit 
    
    print("Welcome to the Contact Manager!\nListed below are the usage commands.\nYou can see them again any time by typing 'commands'\n") # Print a welcome message
    print_usage() # Print the usage for the commands
    # Command Line Interface
    commands = {
        "add": add_contact,
        "list": list_contacts,
        "find": find_contact,
        "del": delete_contact,
        "quit": quit_application,
        "commands": print_usage
    }
    while True:
        command = input("Enter a command: ")
        print() # Print for spacing
        parts = command.split()
        
        if parts[0] in commands:
            try:
                commands[parts[0]](*parts[1:]) # Unpack the rest of the parts and pass them as arguments to the function
                print() # Print an empty line for spacing
            except TypeError:
                print("Invalid number of arguments.") # Print an error message if the number of arguments is invalid
                print_usage_for_command(parts[0]) # Print the usage for the specific command
                print() # Print an empty line for spacing
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print() # Print an empty line for spacing
        else:
            print("Invalid command.") # Print an error message if the command is invalid
            print_usage() # Print the general usage instructions
            print() # Print an empty line for spacing
            
# add command
def add_contact(first_name, last_name, phone_number):
        new_contact = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number    
        }
        
        try:
            with open("db.json", "r") as file: # Open the file in read mode
                data = json.load(file)
        except FileNotFoundError: 
            data = [] # If the file does not exist, create an empty list
            
        data.append(new_contact) # Append the new contact to the list
        
        with open("db.json", "w") as file:
            json.dump(data, file)
            
        print(f"{first_name} {last_name} added to the database.")

# list command        
def list_contacts():
            try:
                with open("db.json", "r") as file:
                    data = json.load(file) # Load the data from the file
            except FileNotFoundError:
                print("No contacts in the database.")
                return # Exit the function if there are no contacts
        
            for contact in data:
                print(f"{contact['first_name']} {contact['last_name']}\n{contact['phone_number']}") # Print the contact
                print("-" * 40) # Print a partition line
# find command       
def find_contact(search_value):
    try:
        with open("db.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No matching contacts found.")
        return # Exit the function if there are no contacts
    
    search_value = search_value.lower() # Convert the search value to lowercase
    
    for contact in data:
        if search_value == contact['first_name'].lower() or search_value == contact['last_name'].lower():
            print(f"{contact['first_name']} {contact['last_name']}\n{contact['phone_number']}\n")
            print("-" * 40)
            return
    
    print("Contact not found.")
    
# delete command
def delete_contact(search_value):
    try:
        with open("db.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No matching contact found.")
        return # Exit the function if there are no contacts
    
    search_value = search_value.lower() # Convert the search value to lowercase
    
    for c, contact in enumerate(data): # Enumerate the data list
        if search_value == contact['first_name'].lower() or search_value == contact['last_name'].lower(): # Check if the search value matches the first or last name
            deleted_contact = data.pop(c) # Remove the contact from the list
            with open("db.json", "w") as file:
                json.dump(data, file) # Write the updated data to the file
                print(f"{deleted_contact['first_name']} {deleted_contact['last_name']} deleted from the database.") # Print the deleted contact
                return
    
    print("No matching contact found.")
    
# quit command         
def quit_application():
        print("Thank you for using the Contact Manager!")
        exit()
        
# Print the usage for the command
def print_usage():
    print("Usage Commands:")
    print("add [fname] [lname] [phone]  (add a new contact record)")
    print("list                         (list all records)")
    print("find [value]                 (find and show the first record that matches the search)")
    print("del [value]                  (delete the first record that matches the search)")
    print("quit                         (quit the CLI)")
    print("commands                     (show usage commands)\n")
    
# Print the usage for a specific command
def print_usage_for_command(command):
    if command == "add":
        print("Usage: add [fname] [lname] [phone]  (add a new contact record)")
    elif command == "list":
        print("Usage: list  (list all records)")
    elif command == "find":
        print("Usage: find [value]  (find and show the first record that matches the search. Search by first name or last name.)")
    elif command == "del":
        print("Usage: del [value]  (delete the first record that matches the search)")
    elif command == "quit":
        print("Usage: quit  (quit the CLI)")
    
if __name__ == "__main__": # Check if the script is being run directly
    main()