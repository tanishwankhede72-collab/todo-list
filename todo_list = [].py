todo_list = []

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(todo_list)):
                print(i + 1, ".", todo_list[i])

    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to delete.")
        else:
            num = int(input("Enter task number to delete: "))
            todo_list.pop(num - 1)
            print("Task deleted successfully!")

    elif choice == "4":
        print("Thank you for using To-Do List App")
        break

    else:
        print("Invalid choice! Try again.")