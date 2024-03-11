def corrects_id(tasks):
    
    for i, task in enumerate(tasks, start=1):
        task[0] = i
    
    return tasks
