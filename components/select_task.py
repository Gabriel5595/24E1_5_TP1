def select_task(tasks, id):
    for task in tasks:
        if task[0] == id:
            return True
    return False

"""
Function:
Receives an ID;
Checks if the ID exists in the DB;

Receives:
* List of tasks
* id
    
Variables:
* id
* task
    
Return:
* True if id is present in the list
* False if id is not present in the list
"""