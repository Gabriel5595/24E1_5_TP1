from tabulate import tabulate

def show_tasks(tasks):
    tasks_header = ["ID", "Description", "Creation Date", "Status", "Deadline", "Urgency"]
    table = tabulate(tasks, headers=tasks_header, tablefmt="grid")
    print("\n")
    print(table)

"""
Function:
Used to show all tasks

Receives:
* list of tasks

Variables:
* tasks

Return:
* Nothing
"""