from fb_operations import add_task, get_tasks, update_task, delete_task

# Handles the task options menu
def manage_tasks():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Quit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            get_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")