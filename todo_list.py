# Define an empty to-do list dictionary
todo_list = {}

# Function to add a task to the to-do list
def add_new_task():
    task = input("Enter a new task: ")
    todo_list[task] = False
    print(f"'{task}' added to the to-do list.")


# Function to view the to-do list
def show_tasks():
    print("To-Do List: ")
    for task, completed in todo_list.items():
        status = "Completed" if completed else "Not Completed"
        print(f"\t{task} - {status}")


# Function to mark a task as completed
def complete_task():
    task = input("Enter the task you have completed: ")
    if task in todo_list:
        todo_list[task] = True
        print(f"'{task}' marked as completed.")
    else:
        print(f"'{task}' task not found.")


# Main program loop
while True:
    print("\nWelcome To To-Do List.")
    print("Chose The Operator.")
    print("1. Add a task.")
    print("2. Mark as completed.")
    print("3. Show the tasks.")
    print("4. Quit.")

    choice = input("Enter the choice [1,2,3,4]: ")

    if choice == "1":
        add_new_task()
    elif choice == "2":
        complete_task()
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid Choice. ")

print("Exiting the program.")