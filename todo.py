tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet!")

    elif choice == '3':
        if tasks:
            try:
                num = int(input("Enter task number to remove: "))
                if 0 < num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Task '{removed}' removed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("No tasks to remove!")

    elif choice == '4':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice!")
