# TaskTrack

TaskTrack is a command-line task management program written in Python. It allows users to view and add tasks, as well as save tasks to a text file so they are available the next time the program runs.

## Current Features

Display a TaskTrack menu.
View all saved tasks.
Add new tasks.
Exit the program through the menu.
Prevent empty tasks from being added.
Remove surrounding whitespace from user input.
Save tasks to a text file.
Load saved tasks when the program starts.
Display a message when there are no tasks.

## Project File description

tasktrack.py — Main Python program containing the TaskTrack functions and menu.
tasks.txt — Text file used to store tasks between program runs.
README.md — Documentation describing the TaskTrack project.

## Requirement

Python 3
A computer running Windows, macOS.
A terminal or command prompt
No additional Python packages are required.

## Running the Program

Run the following command in Terminal:

```Terminal
Open PowerShell or new Terminal
Navigate to the TaskTrack project folder.
Run:
python tasktrack.py

```

## Task Persistence

TaskTrack uses tasks.txt to keep tasks after the program closes.

When the program starts, load_tasks() checks tasks.txt and loads each non-empty line into the task list. When a new task is added, save_tasks() writes the tasks to tasks.txt, with each task stored on its own line.

## Version Control

Git allows changes to be tracked on the computer. A commit saves a group of changes to the local Git history. A push sends committed changes from the local repository to GitHub.

## Current Limitation

When the program closed the task is not saved, the tasks are stored only when the program is running
Tasks can only be added and viewed; they cannot currently be edited or deleted.
Tasks are stored in a simple text file rather than a database.
The program does not currently support task priorities or due dates.
