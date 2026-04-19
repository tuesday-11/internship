
# Simple To-Do List Program with Pre-added Tasks

todo_list = ["Gaming", "Writing", "Reading"]

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(todo_list) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                removed = todo_list.pop(num - 1)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid input.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")