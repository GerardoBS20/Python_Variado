tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task {task} added to the list")

def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    while True:
        try:
            taskToDelete = int(input("Choose the # of the task to delete: "))
            if taskToDelete >= 0 and taskToDelete < len(tasks):
                tasks.pop(taskToDelete)
                print(f"Task #{taskToDelete} deleted")
                break
            else:
                print(f"Task #{taskToDelete} was not found")
        except ValueError:
            print("Invalid input")

def saveTasks():
    with open("tasks.txt", "w") as file:
        for index, task in enumerate(tasks):
            file.write(f"Task #{index}. {task}\n")

def loadTasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    listTasks()

def main():
    loadTasks()
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Delete task")
        print("4. Save tasks")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            listTasks()
        elif choice == "3":
            deleteTask()
        elif choice == "4":
            saveTasks()
        elif choice == "5":
            break
        else:
            print("Invalid option")

main()
