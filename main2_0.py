# major change is that the match statement is replaced with if elif else
# in case user gave add item format
from modules import features
import time as t

date = t.strftime("%d %b, %Y %H:%M:%S")

print(date)
while True:

    i = input("Add, Edit, Done, Remove, Show, Exit : ").strip()
    c = i.lower()
    if c.startswith("add"):
        features.add(i[4:])

    elif c.startswith("edit"):
        try:
            features.modify(int(i[7:]))
        except ValueError:
            print("Enter command as 'edit {integer} '")
            continue

    elif c.startswith("show"):
        features.print_todo()

    elif c.startswith('done'):
        try:
            features.done(int(i[5:]))
        except ValueError:
            print("Enter command as 'done {integer}' ")
            continue

    elif c.startswith('remove'):
        try:
            features.remove(int(i[7:]))
        except ValueError:
            print("Enter command as 'remove {integer}' ")

    elif c.startswith("exit"):
        print("Bye")
        break

    else:
        print("You entered a wrong command.")


