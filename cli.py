from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = (input("Type add, show, edit, complete or exit: ")).strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            row = f"{index + 1}-{item.strip()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos = get_todos()
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            to_remove = todos[number - 1].strip()
            todos.pop(number - 1)
            print(f"Item '{to_remove}' was removed")
            write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("wrong command provided")
