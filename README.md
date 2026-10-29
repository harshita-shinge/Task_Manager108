# Task Manager

A simple command-line task management application built with Python. It allows users to create tasks, track their completion status, and store their tasks between sessions using a JSON file.

## Features

* Add new tasks.
* View all tasks.
* Mark tasks as completed.
* Delete tasks.
* Save tasks locally between sessions.
* Handle invalid menu choices and task numbers.

## Technologies Used

* Python
* JSON for local data storage
* Git and GitHub for version control

## Requirements

* Python 3.10 or later

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/harshita-shinge/Task_Manager108.git
```

### 2. Navigate to the project directory

```bash
cd Task_Manager108
```

### 3. Run the application

```bash
python main.py
```

The application will display a menu in the terminal. Follow the prompts to manage your tasks.

## Data Storage

The application creates a local `tasks.json` file to store task names and completion status.

This file is excluded from Git using `.gitignore`, so each user can maintain their own task list locally.

## Project Structure

```text
Task_Manager108/
├── main.py
├── .gitignore
└── README.md
```

The `tasks.json` file is created locally when tasks are saved and is not included in the repository.

## Learning Objectives

This project demonstrates the use of:

* Python lists and dictionaries
* Functions and loops
* Conditional statements
* Exception handling
* Reading and writing JSON files
* Git and GitHub basics

## Future Improvements

* Add task priorities and due dates.
* Allow users to edit existing tasks.
* Add task search and filtering.
* Develop a graphical user interface.

## Author

Harshita Shinge

GitHub: https://github.com/harshita-shinge
