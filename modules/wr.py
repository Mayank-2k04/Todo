def read_todo(filepath = "files/list.txt"):
    """
    Function reads the contents of the list.txt
     file and returns a list of todos
    :param filepath: files/list.txt
    :return: list of todos
    """
    with open(filepath, "r") as f:
        todo = f.readlines()
    return todo

def write_todo(todo, filepath = "files/list.txt"):
    """
    writes the curent contents of todos
    :param todo: list of items
    :param filepath: files/list.txt
    :return: None
    """
    with open(filepath, "w") as f:
        f.writelines(todo)
# using with context manager is recommended over the second below approach
# file = open("list.txt","r")
"todo = file.readlines()"
# file.close()