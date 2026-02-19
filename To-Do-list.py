#WITHOUT USING JSON
'''
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

'''


#USING JSON

import json
import os



def tasks():
    task = []
    if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:
         with open("tasks.json", "r") as f:
          task = json.load(f)
    else:
         task = [] 
    
    while True:
       
        print(f"\nYou currently have {len(task)} tasks")
        if len(task) > 0:
            for i, t in enumerate(task, 1):
               print(f"{i}. {t['name']} [{t['status']}]")

        print("\nWhat do you want to do?")
        print("1. Add tasks\n2. Delete task\n3. Update task\n4.Mark as Done\n5. Exit/Stop")

        user = int(input("Enter the number to do the operation: "))

        if user == 1:
            user_add=input("Enter the task to add: ")
            if user_add in task:
                print("Task already in the list.")
            else:
              task.append({"name":user_add,"status":"Pending"})

        elif user == 2:
            del_task = input("Enter the task to delete: ")
            for t in task:
             if t["name"] ==del_task:
                task.remove(t)
                print(f"Task '{del_task}' has been deleted")
             else:
                print("Task not found!")

        elif user == 3:
            toUpdate = input("Enter the task to update: ")
            for t in task:
               if t["name"]==toUpdate:
                  updated=input("Enter the task:")
                  t["name"]==updated
               else:
                  print("Task not found!")

        elif user == 5:
            print("Exiting the program----")
            break   # NOW break works
        
        elif user==4:
           mark_task=input("Enter the task name to mark as done:")
           for t in task:
              if t["name"]==mark_task:
                 t["status"]=="Done"
                 print(f"Task '{mark_task}' marked as Done")
              else:
                 print("Task not found")
        else:
            print("Invalid input!")
        with open("tasks.json","w") as f:
          json.dump(task,f,indent=4)



tasks()
