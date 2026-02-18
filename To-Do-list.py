def tasks():
    task = []

    while True:
        print(f"\nYou currently have {len(task)} tasks")
        if len(task) > 0:
            print(task)

        print("\nWhat do you want to do?")
        print("1. Add tasks\n2. Delete task\n3. Update task\n4. Exit/Stop")

        user = int(input("Enter the number to do the operation: "))

        if user == 1:
            user_add=input("Enter the task to add: ")
            if user_add in task:
                print("Task already in the list.")
            else:
              task.append(user_add)

        elif user == 2:
            del_task = input("Enter the task to delete: ")
            if del_task in task:
                task.remove(del_task)
                print(f"Task '{del_task}' has been deleted")
            else:
                print("Task not found!")

        elif user == 3:
            toUpdate = input("Enter the task to update: ")
            if toUpdate in task:
                updated = input("Enter the updated task: ")
                ind = task.index(toUpdate)
                task[ind] = updated
                print("Task updated successfully")
            else:
                print("Task not found!")

        elif user == 4:
            print("Exiting the program----")
            break   # NOW break works

        else:
            print("Invalid input!")

tasks()
