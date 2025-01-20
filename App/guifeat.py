FILEPATH = "list.txt"

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
