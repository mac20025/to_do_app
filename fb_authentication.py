import pyrebase

config = {
    "apiKey": "AIzaSyDbFbwnRB3p9y8ayjJzBUYistOyIGXz574",
    "authDomain": "to-do-list-app-57745.firebaseapp.com",
    "projectId": "to-do-list-app-57745",
    "storageBucket": "to-do-list-app-57745.appspot.com",
    "databaseURL": ""  # Provide an empty string here
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

# Sign in existing user
def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("User signed in successfully!")
        return user  # Return user session information
    except Exception as e:
        print("Failed to sign in:", e)
        return None
