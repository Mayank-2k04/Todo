FILEPATH = "files/list.txt"

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
