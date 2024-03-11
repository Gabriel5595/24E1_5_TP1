def corrects_id(tasks):
    
    for i, task in enumerate(tasks, start=1):
        task[0] = i
    
    return tasks

"""
Function:
Used to correct or add tasks ids

Receives:
* tasks
    
Variables:
* id
* tasks
    
Return:
* Updated list of tasks
"""