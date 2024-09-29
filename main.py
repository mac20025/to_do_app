import getpass
from fb_authentication import sign_up, sign_in
from menu import manage_tasks

def main():
    while True:
        print("\n1. Sign Up\n2. Sign In\n3. Quit")
        auth_choice = input("Enter choice: ")

        if auth_choice == '1':
            email = input("Enter your email: ")
            password = getpass.getpass("Enter your password (input will be hidden): ")
            #getpass will hide the input
            sign_up(email, password)
        elif auth_choice == '2':
            email = input("Enter your email: ")
            password = getpass.getpass("Enter your password (input will be hidden): ")
            user_session = sign_in(email, password)
            if user_session:
                manage_tasks()  # Proceed to task management after authentication
            else:
                print("Authentication failed.")
        elif auth_choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
