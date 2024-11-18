
with open("files/list.txt", "r") as file:
    todo = file.readlines()
# using with context manager is recommended over the second below approach
# file = open("list.txt","r")
"todo = file.readlines()"
# file.close()



def print_todo():
    if len(todo) == 0:
        print("Empty")
        return
    # new_todo = []
    # for ii in todo:
    #     new_todo.append(ii.strip("\n"))

    # using list comprehension

    # new_todo = [item.strip("\n") for item in todo]


    for ii, itm in enumerate(todo):
        print(str(ii+1) + ". " + itm.strip("\n"))

def add():
    todo.append(input("Enter todo : ") + "\n")

def modify():
    if len(todo) == 0:
        print("Empty")
        return

    print_todo()
    index = int(input("Enter todo item to modify : ")) - 1

    if index >= len(todo) or index < 0:
        print("Invalid index")
    else:
        print("Old value: ", todo[index],end="")
        value = input("Enter new value : ") + "\n"
        todo[index] = value
        print("Updated!")
        print_todo()

def done():
    if len(todo) == 0:
        print("Empty")
        return
    ii = int(input("Enter item that is completed: "))-1
    if ii >= len(todo) or ii < 0:
        print("Invalid index")
    else:
        x = todo.pop(ii)
        print("Completed :", x,end="")

def remove():
    if len(todo) == 0:
        print("Empty")
        return

    ii = int(input("Enter item to remove: ")) - 1
    if ii >= len(todo) or ii < 0:
        print("Invalid index")
    else:
        x = todo.pop(ii)
        print("Removed :", x,end="")

while True:
    i = input("Add, Modify, Done, Remove, Show, Exit : ").strip().lower()
    match i:
        case 'add':
            add()
        case 'modify':
            modify()
        case 'show':
            print_todo()
        case 'done':
            done()
        case 'remove':
            remove()
        case 'exit':
            print("Bye")
            break
        case _:
            print("You entered a wrong command.")

    with open("files/list.txt", "w") as file:
        file.writelines(todo)

