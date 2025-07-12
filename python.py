# todo.py

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        
        elif choice == "2":
            new_task = input("Enter task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added.")
        
        elif choice == "3":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {deleted}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
