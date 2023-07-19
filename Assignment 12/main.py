from packages import user_registration
from packages import user_login
from packages import account_management
from packages import file_handling

def main():
    file_handling.create_users_file_if_not_exists()

    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_registration.register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_login.check_credentials(username, password):
                print("Login successful.")
            else:
                print("Invalid username or password.")

        elif choice == "3":
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            account_management.change_password(username, old_password, new_password)

        elif choice == "4":
            username = input("Enter username: ")
            password = input("Enter password: ")
            account_management.delete_account(username, password)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()