def main():
    number = get_input()
    print_row(number)


def get_input():
    while True:
        width = int(input("what is the width? "))
        if width > 0:
            break
    return width


def print_row(width):
    print("?" * width)




main()