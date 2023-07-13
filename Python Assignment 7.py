def append_data_to_file(roll_number, name, class_name, file="data.txt"):
    try:
        with open(file, "a") as f:
            f.writelines([roll_number + "\n", name + "\n", class_name + "\n"])
        with open(file, "r") as f:
            data = f.readlines()
            print("Data in the file:")
            for line in data:
                print(line.strip())
    except IOError as e:
        print("Error: Unable to access the file.")
        print(e)

# Example usage:
append_data_to_file("12345", "John Doe", "Grade 10")