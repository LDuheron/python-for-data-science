def NULL_not_found(object: any) -> int:
    """Prints the objects of all types of "Null"."""
    obj_type = type(object)

    if object != object:
        print(f'Cheese: {object} {obj_type}')
        return 0

    if object is False:
        print(f'Fake: {object} {obj_type}')
        return 0

    is_null = {
        'Zero': 0,
        'Empty': "",
        'Nothing': None
        }

    for key, value in is_null.items():
        if object == value:
            print(f'{key}: {value} {obj_type}')
            return 0

    print("Type not Found")
    return 1
