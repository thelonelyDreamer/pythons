def read_file(path: str):
    with open(path) as file_object:
        contents = file_object.read()
    return contents
