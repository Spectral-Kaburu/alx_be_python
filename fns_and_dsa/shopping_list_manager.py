def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)  # Convert choice to integer

        if choice == 1:
            # Prompt for and add an item
            addition = input("Enter the item to add: ").lower()
            shopping_list.append(addition)
        elif choice == 2:
            # Prompt for and remove an item
            remove = input("Enter the item to be removed: ").lower()
            if remove in shopping_list:
                shopping_list.remove(remove)
            else:
                print(f"{remove} is not in the shopping list.")
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for i in shopping_list:
                    print(f"- {i}")
            else:
                print("The shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
