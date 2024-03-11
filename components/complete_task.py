from components.select_task import select_task

def complete_task(tasks):
    
    selected_id = int(input("\nEnter the task ID number: "))
    task_exists = select_task(tasks, selected_id)
    
    if task_exists:
        tasks[selected_id-1][3] = "Finished"
        return tasks
    else:
        print("No task could found with the entered ID.")

"""
Function:
change the status of a task

Receives:
* id returned by the function select_task

Variables:
* id
* tasks

Return:
* Updated list of tasks
"""