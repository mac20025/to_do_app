import firebase_admin
from firebase_admin import credentials, firestore

# Path to service account key JSON file
cred = credentials.Certificate('C:/Users/rbarc/OneDrive/Documentos/Educação/Graduação/BYU-I/2024 03/CSE 310/W04/to-do-list-app-57745-firebase-adminsdk-hqf6b-3cef2b5b34.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

#Use the set() method to create or update a task in Firestore
def add_task():
    task_id = get_next_task_id()
    task_name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    
    db.collection('tasks').document(str(task_id)).set({
        'id': task_id,  # Store the task ID
        'name': task_name,
        'description': description,
        'due_date': due_date,
        'completed': False
    })
    print(f"Task '{task_name}' added with ID {task_id} successfully!")


#Use the get() method to retrieve tasks
def get_tasks():
    tasks = db.collection('tasks').stream()
    for task in tasks:
        task_data = task.to_dict()
        print(f"ID: {task_data['id']}, Name: {task_data['name']}, Description: {task_data['description']}, Due Date: {task_data['due_date']}, Completed: {task_data['completed']}")


#Use update() to modify a task
def update_task():
    task_id = input("Enter task ID to update: ")
    completed = input("Is the task completed? (yes/no): ").lower() == 'yes'
    
    task_ref = db.collection('tasks').document(task_id)
    task_ref.update({
        'completed': completed
    })
    print(f"Task ID {task_id} updated successfully!")


#Use delete() to remove a task
def delete_task():
    task_id = input("Enter task ID to delete: ")
    
    task_ref = db.collection('tasks').document(task_id)
    task_ref.delete()
    print(f"Task ID {task_id} deleted successfully!")


#Retrieve the current highest task ID to increments it
def get_next_task_id():
    tasks = db.collection('tasks').order_by('id', direction=firestore.Query.DESCENDING).limit(1).stream()
    for task in tasks:
        return task.to_dict().get('id') + 1
    return 1  # If no tasks, start with ID 1