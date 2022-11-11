import json


def fun(file: str):
    try:
        with open(file) as f:
            username = json.load(f)
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        username = None
    else:
        pass
    finally:
        pass
    return username