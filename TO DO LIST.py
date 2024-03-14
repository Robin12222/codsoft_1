def display_menu():
    print("Menu:")
    print("1. Enter task")
    print("2. Display task")
    print("3. Done task ")
    print("4. Quit")


def Enter_task(tasks):
    task = input("Enter yourtask: ")
    tasks.append(task)
    print("Task added ")


def Display_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def Done(tasks):
    if not tasks:
        print("No tasks left.")
        return


    Display_tasks(tasks)
    index = int(input("Enter task index to mark as done: ")) - 1


    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' is done and removed.")
    else:
        print("Invalid task index.")


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()


    while True:
        display_menu()


        choice = input("Enter your choice: ")


        if choice == '1':
            Enter_task(tasks)
        elif choice == '2':
            Display_tasks(tasks)
        elif choice == '3':
            Done(tasks)
        elif choice == '4':
            print("Exiting.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
