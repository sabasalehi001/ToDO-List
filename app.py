# Display the list of tasks
def display_tasks():
    if len(tasks) == 0:
        print("No tasks.")
    else:
        print("Tasks:")
        for task in tasks:
            print("- " + task)

# Add a new task
def add_task(task):
    tasks.append(task)
    print("Task added.")

# Remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

# Exit the program
def exit_program():
    print("Exiting program.")
    exit()

# Main program loop
tasks = []
while True:
    print("Enter '1' to display tasks.")
    print("Enter '2' to add a task.")
    print("Enter '3' to remove a task.")
    print("Enter '4' to exit the program.")
    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "3":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "4":
        exit_program()
    else:
        print("Invalid choice. Please try again.")
