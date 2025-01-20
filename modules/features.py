FILEPATH = "../files/list.txt"

def read_todo(filepath = FILEPATH):
    """
    Function reads the contents of the list.txt
     file and returns a list of todos
    :param filepath: files/list.txt
    :return: list of todos
    """
    with open(filepath, "r") as f:
        todo = f.readlines()
    return todo


def write_todo(todo, filepath = FILEPATH):
    """
    writes the curent contents of todos
    :param todo: list of items
    :param filepath: files/list.txt
    :return: None
    """
    with open(filepath, "w") as f:
        f.writelines(todo)


def print_todo():
    todo = read_todo()
    if len(todo) == 0:
        print("Empty")
        return
    for ii, itm in enumerate(todo):
        print(str(ii+1) + ". " + itm.strip("\n"))


def add(n):
    if len(n) == 0 or n.isspace():
        print("Enter an item to add.")
        return

    todo = read_todo()
    todo.append(n + "\n")
    write_todo(todo)


def modify(index):
    todo = read_todo()
    if len(todo) == 0:
        print("Empty")
        return
    index -= 1
    if index >= len(todo) or index < 0:
        print("Invalid index")
    else:
        print("Old value: ", todo[index],end="")
        value = input("Enter new value : ") + "\n"
        todo[index] = value

        write_todo(todo)

        print("Updated!")
        print_todo()


def done(ii):
    todo = read_todo()
    if len(todo) == 0:
        print("Empty")
        return
    ii -= 1
    try:
        x = todo.pop(ii)
        write_todo(todo)
        print("Completed :", x,end="")
    except IndexError:
        print("Enter a valid index")


def remove(ii):
    todo = read_todo()
    if len(todo) == 0:
        print("Empty")
        return
    ii -= 1
    try:
        x = todo.pop(ii)
        write_todo(todo)
        print("Removed :", x,end="")
    except IndexError:
        print("Enter a valid index")

# if __name__ == "__main__":
#     print("Hi")