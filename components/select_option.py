from components.create_task import create_task
from components.add_task import add_task
from components.show_tasks import show_tasks
from components.complete_task import complete_task
from components.delete_task import delete_task

def select_option():
    tasks = []
    
    while True:
        try:
            print("""\nSelect one of the option below:
1. Add task
2. Show tasks
3. Set task to 'finished'
4. Delete task
5. Exit""")
            
            option = int(input("\nPlease, enter the option number: "))
            
            if option == 1:
                new_task = create_task(tasks)
                tasks = add_task(new_task, tasks)
            elif option == 2:
                show_tasks(tasks)
            elif option == 3:
                tasks = complete_task(tasks)
            elif option == 4:
                tasks = delete_task(tasks)
            elif option == 5:
                print("Exiting...")
                break
            else:
                print("Option not valid. Please, enter a valid option.")
            
        except ValueError:
            ("Option not valid. Please enter a number correspondent to a valid option.")

"""
Function:
Used to present the possible options to the user;
Based on the options, a part of the will be initialized.

Receives:
* nothing
    
Variables:
* tasks
* option
    
Return:
* Nothing
"""