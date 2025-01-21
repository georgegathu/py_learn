class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def remove_task(self):
        task = input("Enter a task to remove: ")
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed!")
        else:
            print(f"Task '{task}' not found!")

    def mark_task_completed(self):
        task = input("Enter a task to mark as completed: ")
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' marked as completed!")
        else:
            print(f"Task '{task}' not found!")

    def display_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            print(f"- {task}")

todo_list = ToDoList()
while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task as completed")
    print("4. Display tasks")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        todo_list.add_task()
    elif choice == "2":
        todo_list.remove_task()
    elif choice == "3":
        todo_list.mark_task_completed()
    elif choice == "4":
        todo_list.display_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
