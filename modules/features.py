from modules import wr


def print_todo():
    todo = wr.read_todo()
    if len(todo) == 0:
        print("Empty")
        return
    for ii, itm in enumerate(todo):
        print(str(ii+1) + ". " + itm.strip("\n"))


def add(n):
    if len(n) == 0 or n.isspace():
        print("Enter an item to add.")
        return

    todo = wr.read_todo()
    todo.append(n + "\n")
    wr.write_todo(todo)

def modify(index):
    todo = wr.read_todo()
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

        wr.write_todo(todo)

        print("Updated!")
        print_todo()

def done(ii):
    todo = wr.read_todo()
    if len(todo) == 0:
        print("Empty")
        return
    ii -= 1
    try:
        x = todo.pop(ii)
        wr.write_todo(todo)
        print("Completed :", x,end="")
    except IndexError:
        print("Enter a valid index")

def remove(ii):
    todo = wr.read_todo()
    if len(todo) == 0:
        print("Empty")
        return
    ii -= 1
    try:
        x = todo.pop(ii)
        wr.write_todo(todo)
        print("Removed :", x,end="")
    except IndexError:
        print("Enter a valid index")

# if __name__ == "__main__":
#     print("Hi")