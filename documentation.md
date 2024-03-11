# Documentation
## create_task (tasks)
#### Function:
Used to create a new task.

#### Receives:
* tasks
    
#### Variables:
* id
* description
* creationDate
* status
* deadline
* urgency
    
#### Returns:
* List named "new_task"


## add_task (new_task , tasks)
#### Function:
Used to add the list returned from function create_task and add it to the tasks list.

#### Receives:
* new_task list from create_task
* tasks list
    
#### Variables:
* new_task
* tasks
* updated_tasks
    
#### Return:
* updated_tasks

## select_task (tasks)
#### Function:
Receives an ID;
Checks if the ID exists in the DB;

#### Receives:
* List of tasks
* id
    
#### Variables:
* id
* task
    
#### Return:
* True if id is present in the list
* False if id is not present in the list

## show_tasks (tasks)
#### Function:
Used to show all tasks

#### Receives:
* list of tasks
    
#### Variables:
* tasks
    
#### Return:
* Nothing

## complete_task (id, tasks)
#### Function:
change the status of a task

#### Receives:
* id returned by the function select_task
    
#### Variables:
* id
* tasks
    
#### Return:
* Updated list of tasks

## delete_task (id, tasks)
#### Function:
Used to delete a task

#### Receives:
* id returned by the function select_task
    
#### Variables:
* id
* tasks
    
#### Return:
* Updated list of tasks

## select_option ()
#### Function:
Used to present the possible options to the user;
Based on the options, a part of the will be initialized.

#### Receives:
* nothing
    
#### Variables:
* tasks
* option
    
#### Return:
* Nothing

## corrects_id (tasks)
#### Function:
Used to correct or add tasks ids

#### Receives:
* tasks
    
#### Variables:
* id
* tasks
    
#### Return:
* Updated list of tasks