def create_users_file_if_not_exists():
    try:
        with open("users.txt", "x"):
            pass
    except FileExistsError:
        pass