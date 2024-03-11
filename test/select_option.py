from create_task import create_task
from add_task import add_task
from show_tasks import show_tasks
from complete_task import complete_task
from delete_task import delete_task

def select_option():
    tasks = [
    [1, "Task 1 Description", "01/03/2024", "Ongoing", "15/03/2024", "High"],
    [2, "Task 2 Description", "02/03/2024", "Finished", "10/03/2024", "Medium"],
    [3, "Task 3 Description", "03/03/2024", "Ongoing", "20/03/2024", "Low"],
    [4, "Task 4 Description", "04/03/2024", "Finished", "12/03/2024", "High"],
    [5, "Task 5 Description", "05/03/2024", "Ongoing", "18/03/2024", "Medium"],
    [6, "Task 6 Description", "06/03/2024", "Ongoing", "25/03/2024", "Low"],
    [7, "Task 7 Description", "07/03/2024", "Finished", "08/03/2024", "High"],
    [8, "Task 8 Description", "08/03/2024", "Ongoing", "16/03/2024", "Medium"],
    [9, "Task 9 Description", "09/03/2024", "Finished", "14/03/2024", "Low"],
    [10, "Task 10 Description", "10/03/2024", "Ongoing", "22/03/2024", "High"],
    [11, "Task 11 Description", "11/03/2024", "Ongoing", "19/03/2024", "Medium"],
    [12, "Task 12 Description", "12/03/2024", "Finished", "09/03/2024", "Low"],
    [13, "Task 13 Description", "13/03/2024", "Ongoing", "17/03/2024", "High"],
    [14, "Task 14 Description", "14/03/2024", "Finished", "11/03/2024", "Medium"],
    [15, "Task 15 Description", "15/03/2024", "Ongoing", "23/03/2024", "Low"],
    [16, "Task 16 Description", "16/03/2024", "Ongoing", "21/03/2024", "High"],
    [17, "Task 17 Description", "17/03/2024", "Finished", "13/03/2024", "Medium"],
    [18, "Task 18 Description", "18/03/2024", "Ongoing", "26/03/2024", "Low"],
    [19, "Task 19 Description", "19/03/2024", "Finished", "16/03/2024", "High"],
    [20, "Task 20 Description", "20/03/2024", "Ongoing", "24/03/2024", "Medium"]
]
    
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

select_option()