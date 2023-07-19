def change_password(username, old_password, new_password):
    with open("users.txt", "r") as file:
        lines = file.readlines()

    with open("users.txt", "w") as file:
        for line in lines:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and old_password == stored_password:
                file.write(f"{username},{new_password}\n")
                print("Password changed successfully.")
            else:
                file.write(line)

def delete_account(username, password):
    with open("users.txt", "r") as file:
        lines = file.readlines()

    with open("users.txt", "w") as file:
        for line in lines:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                print("Account deleted successfully.")
            else:
                file.write(line)