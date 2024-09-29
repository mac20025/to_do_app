# Overview

A simple project that connects Python to a Firebase database that stores
tasks in a to do list.

I've created this software to demonstrate how to use Python to connect to a cloud database.

# Development Environment

For this software, I used:
- Visual Studio Code 1.91.1
- Python 3.10
- firebase_admin
- pyrebase
- getpass

# The project has 4 files:
- fb_authentication.py: Contains the code that will authenticate the user
- fb_operations.py: Stores the functions that handle database operations
- menu.py: A function that manages the menu operations
- main.py: Gets the program running

# Features
- User authentication via email and password (Firebase Authentication)
- Task management:
  - Add new tasks with a description and due date
  - View all tasks
  - Update task status (completed or not)
  - Delete tasks

# Installation Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


# Useful Websites

* [Visual Studio Code](https://code.visualstudio.com/)
* [Python](https://www.python.org/)
* [Firebase](https://console.firebase.google.com/)