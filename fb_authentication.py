import pyrebase

config = {
    "apiKey": "AIzaSyDbFbwnRB3p9y8ayjJzBUYistOyIGXz574",
    "authDomain": "to-do-list-app-57745.firebaseapp.com",
    "projectId": "to-do-list-app-57745",
    "storageBucket": "to-do-list-app-57745.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Sign up new user
def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("User created successfully!")
    except Exception as e:
        print(e)
