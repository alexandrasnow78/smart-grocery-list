print("Welcome to the Smart Grocery App!\n\nWhat would you like to do?")

def show_menu():
    action = input("\n1. Add an item\n2. View your grocery list\n3. Remove an item\n4. Exit\n\nEnter your choice: ")
    return action

def add_item(items):
    new_item = input("\nWhat grocery item would you like to add to your list? ")
    items.append(new_item)
    print(f"Item added to the list: {new_item}")

def view_list(items):
    if items == []:
        print("Your list is empty!\n")
    else:
        print("\n=====YOUR GROCERY LIST=====")
        for number, item in enumerate(items, start =1):
            print(f"\n{number}. {item}")
        print("\n===========================")

def remove_item(items):
    if items == []:
        print("Your list is empty! Nothing to remove.\n")
    else:
        item_to_remove = input("Which item would you like to remove from your list? ")
        for grocery_item in items:
            #Allow user to remove items regardless of capitalization
            if grocery_item.lower() == item_to_remove.lower():
                items.remove(grocery_item)
                print(f"Item removed from the list: {item_to_remove}")
                break
        else:
            print(f"{item_to_remove} is not in your grocery list.")

def load_list():
    try:
        file = open("groceries.txt", "r")
        lines = file.readlines()
        file.close()

        grocery_items = []

        for line in lines:
            grocery_items.append(line.strip())
        return grocery_items

    #Start with an empty list if no saved file exists        
    except FileNotFoundError:
        return []

#Load saved grocery items when the program starts
grocery_list = load_list()

def save_list(items):
    file = open("groceries.txt", "w")
    for line in items:
        file.write(line + "\n")
    file.close()

while True:
    action = show_menu()

    if action == "1":
        add_item(grocery_list)
    elif action == "2":
        view_list(grocery_list)
    elif action == "3":
        remove_item(grocery_list)
    elif action == "4":
        #Save changes before closing the application
        save_list(grocery_list)
        print("Exiting the Smart Grocery App. Goodbye!")
        break
    else:
        print("Invalid option. Please choose '1', '2', '3', or '4'.")