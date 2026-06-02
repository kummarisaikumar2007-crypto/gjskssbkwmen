def display_menu():
    print("\n--- MY INTERNSHIP TO-DO LIST ---")
    print("1. View Current Tasks")
    print("2. Add a New Task")
    print("3. Delete a Task")
    print("4. Exit Application")


def main():
    task_list = []

    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            if not task_list:
                print("\nYour to-do list is completely empty!")
            else:
                print("\n--- YOUR CURRENT TASKS ---")
                for index, task in enumerate(task_list, start=1):
                    print(f"{index}. {task}")

        elif choice == "2":
            new_task = input("\nType the task you want to add: ").strip()
            if new_task:
                task_list.append(new_task)
                print(f"'{new_task}' has been added successfully.")
            else:
                print("Task cannot be blank!")

        elif choice == "3":
            if not task_list:
                print("\nNothing to delete. Your list is empty!")
            else:
                print("\n--- YOUR CURRENT TASKS ---")
                for index, task in enumerate(task_list, start=1):
                    print(f"{index}. {task}")

                try:
                    task_num = int(
                        input("\nEnter the number of the task to delete: ")
                    )
                    if 1 <= task_num <= len(task_list):
                        removed = task_list.pop(task_num - 1)
                        print(f"Removed task: '{removed}'")
                    else:
                        print("Invalid number. No task found at that position.")
                except ValueError:
                    print("Please type a valid number.")

        elif choice == "4":
            print("\nExiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
