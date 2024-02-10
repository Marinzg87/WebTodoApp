FILEPATH = r"/Users/marcinbogusz/Desktop/Python/Python_Udemy_Learn_in_60_Days_Build_20_Apps/WebApp_ToDo/WebApp_ToDo/todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# the way to run file directly, not when it's imported
if __name__ == "__main__":
    print(get_todos())
