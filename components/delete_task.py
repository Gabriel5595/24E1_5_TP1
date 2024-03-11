from components.select_task import select_task
from components.corrects_id import corrects_id

def delete_task(tasks):
    selected_id = int(input("\nEnter the task ID number: "))
    task_exists = select_task(tasks, selected_id)
    
    if task_exists:
        tasks.pop(selected_id-1)
        updated_tasks = corrects_id(tasks)
        return updated_tasks
    else:
        print("No task could found with the entered ID.")