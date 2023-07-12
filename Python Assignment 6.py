def ds(roll_no, name):
    # List
    my_list = [roll_no, name]

    # Tuple
    my_tuple = (roll_no, name)

    # Set
    my_set = {roll_no, name}

    # Dictionary
    my_dict = {'roll_no': roll_no, 'name': name}

    # Change values during runtime
    name2 = "Aadit"
    rollno2 = 114
    
    #changing list items
    list[0] = name2
    list[1] = rollno2
    print("Updated List:", list)
    
    #changing tuple items
    tuple = (name2,rollno2)
    print("Updated Tuple:", tuple)
    
    #changing set items
    set.remove(name)
    set.remove(roll_no)
    set.add(name2)
    set.add(rollno2)
    print("Updated Set:", set)
    
    #changing dictnory items
    dict["name"] = name2
    dict["rollno"] = rollno2
    print("Updated Dictionary:", dict)

    
 # Deleting the data structures
    del list
    del tuple
    del set
    del dict
ds("Arpit" ,64)