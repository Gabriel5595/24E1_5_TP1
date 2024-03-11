from datetime import datetime

def create_task(tasks):
    
    id = len(tasks) + 1
    description = input("\nAdd a description for this task: ")
    creationDate = datetime.now().date().strftime('%d/%m/%Y')
    status = "Ongoing"
    deadline = input("Add a dealine for this task (DD/MM/YYYY): ")
    urgency = input("Add a level of urgency: ")
    
    new_task = [id, description, creationDate, status, deadline, urgency]
    
    return new_task

"""
Function:
Used to create a new task.

Receives:
* tasks

Variables:
* id
* description
* creationDate
* status
* deadline
* urgency

Returns:
* List named "new_task"
"""