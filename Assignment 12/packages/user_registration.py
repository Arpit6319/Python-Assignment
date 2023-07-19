def register_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("User registered successfully.")