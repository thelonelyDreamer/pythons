from read import read_file


def file():
    content: str = read_file("resource/x.txt")
    str_list = content.split("\n")
    for r in str_list:
        print(len(r), end="")


if __name__ == '__main__':
    file()
    print("a b ".split(" "))
