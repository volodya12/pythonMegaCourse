

agenda = []

while True:
    user_input = input("What is on agenda? Option: show, add, remove, edit, exit: ").strip().lower()

    if user_input == 'add':
        new_item = input("What do you want to add? ")+'\n'
        agenda.append(new_item)  # adds to the List
        file = open(r"todo.txt", 'w') # declare file as 'write'
        file.writelines(agenda)     # write list to file
        file.close()
    elif user_input == 'remove':
        remove_item = input("Which item you want to remove? Type show - to show list")
        for todos in agenda:
            print(todos)
        agenda.remove(remove_item) #removes item by name
            #remove_element = agenda.pop(1) #removes by index
        print("Removed element: ", remove_item)

    elif user_input == 'show':
        file = open("todo.txt", 'r')    # declaring file as read
        file.readlines()                # reading lines BUT will not display in console
        file.close()
        for index, item in enumerate(agenda):   # since file has read lines, now need to display in Console
            item = item.strip('\n')
            row = f"{index+1}.{item}"
            print(row)

    elif user_input == 'edit':
        number = int(input("Number of the item you want replace? "))
        number = number - 1

        with open('todo.txt', 'r') as file:
            agenda = file.readlines()

        replaced_item = input("What do you want to replace with? ")+'\n'
        agenda[number] = replaced_item

        with open('todo.txt', 'w') as file:
            file.writelines(agenda)

    elif user_input == 'exit':
        break














































