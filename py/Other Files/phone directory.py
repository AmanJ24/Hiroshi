directory = {}
is_on = True

print("Welcome to Telephone Directory.")

while is_on:
    print('''
    A = Add new records to the directory
    S = Search records from the directory
    M = Modify records in the directory
    D = Delete records from the directory
    Q = Quit
    ''')

    action = input("What would you like to do?: ")

    if action == 'A':
        new_name = input("Add the name: ")
        new_num = input("Enter the phone number: ")
        if len(new_num) == 10:
            directory[new_name] = new_num 
            print("Your contact was added successfully.")
        else:
            print("Please write a 10-digit number.")    

    elif action == 'S':
        search = input("Search the contact name: ")
        if search not in directory:
            print("The searched contact is not available.")
        else:    
            print(f"{search}: {directory[search]}")

    elif action == 'M':
        name = input("Enter the contact you want to modify: ")
        if name in directory:
            new_number = int(input("Enter the new number: "))
            directory[name] = new_number
            print("Number modified successfully.")
        else:
            print("The inputed number was not found.")    

    elif action == 'D':
        delete = input("Enter the contact you want to delete: ")
        if delete in directory:
            directory.pop(delete)
            print("The number was successfully deleted.")

    elif action == 'Q':
        print("Goodbye!")
        is_on = False    