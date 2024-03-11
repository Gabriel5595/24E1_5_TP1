def select_task(tasks, id):
    for task in tasks:
        if task[0] == id:
            return True
    return False