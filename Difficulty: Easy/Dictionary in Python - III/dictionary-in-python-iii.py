# insert into dictionary
def insert_dict(query, dict):
    # Your code here
    operation, key, value = query
    dict[key] = value
    return 'Inserted'
    

# deleting from dictionary
def del_dict(query, dict):
    # Your code here
    operation, key = query
    del dict[key]
    return "Deleted"
    

# print marks of required name
def print_dict(key, dict):
    # Your code here
    if key in dict:
        print(f"Marks of {key} is {dict[key]}")
    else:
        print("-1")