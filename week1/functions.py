contacts = []
tasks = []

# Contact Book :

def add_contact():
    name = input("Enter Name: ")
    number = input("Enter Number: ")
    contact = {"Name": name, "Number": number}
    contacts.append(contact)
    print("Contact Added")


def find_contact():
    name = input("Enter Name to Search: ")
    for i in contacts:
        if i["Name"] == name:
            print("Contact Found:", i)
            return       
    print("Contact Not Found")


def list_contacts():
    if len(contacts) == 0:
        print("No Contacts Available")
    else:
        for i in contacts:
            print(i)


# To-Do List :
def add_task():
    task = input("Enter Task: ")
    tasks.append(task)
    print("Task Added")
    
def remove_task():
    task = input("Enter Task to Remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task Removed")
    else:
        print("Task Not Found")


def show_tasks():
    if len(tasks) == 0:
        print("No Tasks Available")
    else:
        print("Tasks:")
        for i in tasks:
            print(i)



while True:
    print("\n1. Contact Book")
    print("2. To-Do List")
    print("3. Exit")

    choice = int(input("Enter Choice: "))
    if choice == 1:
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. Find Contact")
            print("3. List Contacts")
            print("4. Back")

            ch = int(input("Enter Choice: "))
            if ch == 1:
                add_contact()
            elif ch == 2:
                find_contact()
            elif ch == 3:
                list_contacts()
            elif ch == 4:
                break
            else:
                print("Invalid Choice")

    elif choice == 2:

        while True:
            print("\n--- To-Do List ---")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Show Tasks")
            print("4. Back")

            ch = int(input("Enter Choice: "))
            if ch == 1:
                add_task()
            elif ch == 2:
                remove_task()
            elif ch == 3:
                show_tasks()
            elif ch == 4:
                break
            else:
                print("Invalid Choice")

    elif choice == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")