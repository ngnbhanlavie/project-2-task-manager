import json
from rich.console import Console
from rich.table import Table
import argparse

console=Console()

class Task:
    def __init__(self,title: str,no: int,des: str,completed:bool=False):
        self.title=title
        self.id=no
        self.description=des
        self.completed=completed

        if no<0:
            raise ValueError("Task ID must be positive")
        if not title.strip():
            raise ValueError("Task title cannot be empty")

    def complete(self)->None:
        self.completed=True

    def to_dict(self)->dict:
        return{
            "id":self.id,
            "title": self.title,
            "description":self.description,
            "completed":self.completed
        }

def main():
    parser=argparse.ArgumentParser(description="A simple command-line task manager")
    subparsers=parser.add_subparsers(dest="command",required=True)

    add_parser=subparsers.add_parser(
        "add",
        help="Add a new task"
    )
    add_parser.add_argument(
        "title",
        help="Title of the task"
    )

    view_parser=subparsers.add_parser(
        "view",
        help="View all tasks"
    )

    complete_parser=subparsers.add_parser(
        "complete",
        help="Mark a task as completed"
    )
    complete_parser.add_argument(
        "id",
        type=int,
        help="ID of the task to complete"
    )

    delete_parser=subparsers.add_parser(
        "delete",
        help="Delete a task"
    )
    delete_parser.add_argument(
        "id",
        type=int,
        help="ID of the task to delete"
    )
    
    args=parser.parse_args()
    tasks=load()

    if args.command=="add":
        add_task(tasks,args.title)
    elif args.command=="view":
        view_task(tasks)
    elif args.command=="complete":
        complete_task(tasks,args.id)
    elif args.command=="delete":
        delete_task(tasks,args.id)

    save(tasks)


def load()->list[Task]:
    try:
        with open("task.json","r") as file:
            data=json.load(file)

        tasks: list[Task]=[]

        for item in data:
            task=Task(
                item["title"],
                item["id"],
                item["description"],
                item["completed"]
            )

            tasks.append(task)

        return tasks
    except FileNotFoundError:
        return[]

def save(tasks: list[Task]) -> None:
    data=[]
    for task in tasks:
        data.append(task.to_dict())

    with open("task.json","w") as file:
        json.dump(data,file,indent=4)

def add_task(tasks: list[Task],title: str)->None:
        if title is None:
            print("Please provide a task title.")
            return
        
        if tasks:
            no=max(task.id for task in tasks)+1
        else:
            no=1
        
        des=input("Description:")
        task=Task(title,no,des)
        tasks.append(task)
        print("Task added successfully")


def view_task(tasks: list[Task])->None:
    table=Table(title="My Tasks")

    table.add_column("ID")
    table.add_column("TASK")
    table.add_column("DESCRIPTION")
    table.add_column("STATUS")

    for task in tasks:
        status="Done" if task.completed else "Pending"

        table.add_row(
            str(task.id),
            task.title,
            task.description,
            status
        )

    console.print(table)

def complete_task(tasks:list[Task],task_id:int)->None:
    for task in tasks:
        if task.id==task_id:
            task.complete()
            print("Task completed")
            return
    print("Task not found")

def delete_task(tasks:list[Task],task_id:int)->None:
    for task in tasks:
        if task.id==task_id:
            tasks.remove(task)
            print("Task deleted")
            return
    print("Task not found")

if __name__=="__main__":
    main()
