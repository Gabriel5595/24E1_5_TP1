from select_task import select_task

def complete_task(tasks):
    
    selected_id = int(input("\nEnter the task ID number: "))
    task_exists = select_task(tasks, selected_id)
    
    if task_exists:
        tasks[selected_id-1][3] = "Finished"
        return tasks
    else:
        print("No task could found with the entered ID.")