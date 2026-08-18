# Python Task Manager

A command-line task manager built with Python.

This project allows users to create, view, complete, and delete tasks while storing task data in a JSON file.

## Features

- Add tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Store tasks in JSON
- Command-line interface with argparse
- Rich table output
- Automated tests with pytest
- Static type checking with mypy

## Technologies

- Python
- argparse
- JSON
- Rich
- pytest
- mypy
- Git / GitHub

## Usage
### Add a task
```bash
python main.py add "Learn Python"
```
### Complete a task
```bash
python main.py complete 1
```
### Delete a task
```bash
python main.py delete 1
```
### Show help
```bash
python main.py --help
```
### Testing
```bash
python -m mypy main.py
```

### View tasks
```bash
python main.py view